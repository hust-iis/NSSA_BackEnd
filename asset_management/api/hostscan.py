from http import HTTPStatus
from response import CustomResponse, ERROR_CODES, ERROR_MESSAGES

from asset_management.models import *
from asset_management.scan.nmap_alive import scanNetwork
from asset_management.serializers import AssetSerializer
from risk_analysis.models import AssetRisk
from rest_framework.response import Response
from rest_framework.views import APIView

import json
from django.db.models import Q
from django.core import serializers
from django.http import JsonResponse
from rest_framework import status
from asset_management.scan.multiScan import multiScan


class AssetScan(APIView):

    def get(self, request):
        res = Asset.objects.all()
        ser = AssetSerializer(instance=res, many=True)
        return Response(ser.data)

    def post(self, request):
        data = request.data
        network = data['netSeg']  # 扫描的目标网段
        speed = data['maxThreadNum']  # nmap扫描速度等级
        portRange = data['portRange']  # nmap扫描端口范围
        arguments = '-sV -O -p ' + str(portRange) + ' -T' + str(speed)
        try:
            infos = multiScan(network, arguments)
            infoslen = len(infos)
            print("-------------")
            print(infos)
        except Exception as e:
            print(e)
            print('扫描过程中出错')
            return CustomResponse(
                code=ERROR_CODES['INTERNAL_SERVER_ERROR'],
                msg=ERROR_MESSAGES['INTERNAL_SERVER_ERROR'],
                data={},
                status=HTTPStatus.INTERNAL_SERVER_ERROR
            )
        try:
            for info in infos:
                addToDB(info)
        except Exception as e:
            print(e)
            print('扫描信息入库失败')
            return CustomResponse(
                code=ERROR_CODES['INTERNAL_SERVER_ERROR'],
                msg=ERROR_MESSAGES['INTERNAL_SERVER_ERROR'],
                data={},
                status=HTTPStatus.INTERNAL_SERVER_ERROR
            )
        # asset_list = Asset.objects.all()
        # asset_list = json.loads(serializers.serialize("json", asset_list))
        return CustomResponse(
            data={
                "total": infoslen
            }
        )


def addToDB(info):  # 分析单机扫描的结果，将主机信息和主机服务信息添加进数据库
    qs = Asset.objects.filter(ip=info['ip'])  # 在数据库中查找对应ip的主机
    if len(qs) == 0:  # 如果不存在,则直接插入
        h1 = Asset(ip=info['ip'], name=info['hostname'], device_vendor=info['vendor'], device_type=info['type'],
                   os=info['os'], mac=info['mac'], update_time=info['update_time'])
        h1.save()
    else:  # 如果已经存在,则更新字段值
        h1 = Asset.objects.get(ip=info['ip'])
        h1.asset_name = info['hostname']
        h1.device_vendor = info['vendor']
        h1.device_type = info['type']
        h1.os = info['os']
        h1.mac = info['mac']
        h1.update_time = info['update_time']
        h1.save()
    # 资产风险表处理
    qs = AssetRisk.objects.filter(asset_id=h1.id)
    if len(qs) == 0:  # 如果不存在,则直接插入；如果存在，则不做额外操作
        r1 = AssetRisk(asset_id=h1.id)
        r1.save()
    #
    for tcp_port in info['tcp_ports']:
        qs = AssetService.objects.filter(ip=info['ip'], port=tcp_port)  # 在数据库中查找对应ip和端口的主机服务信息
        asset_chosen = Asset.objects.get(ip=info['ip'])
        asset_id_temp = asset_chosen.id
        if len(qs) == 0:  # 如果不存在,则直接插入
            s1 = AssetService(asset_id=asset_id_temp, ip=info['ip'], port=tcp_port, state=info[tcp_port]['state'],
                              name=info[tcp_port]['name'], product=info[tcp_port]['product'],
                              version=info[tcp_port]['version'], cpe=info[tcp_port]['cpe'],
                              extrainfo=info[tcp_port]['extrainfo'], update_time=info['update_time'])
            s1.save()
        else:  # 如果已经存在,则更新字段值
            s1 = AssetService.objects.get(ip=info['ip'], port=tcp_port)
            s1.state = info['state']
            s1.name = info[tcp_port]['name']
            s1.product = info[tcp_port]['product']
            s1.version = info[tcp_port]['version']
            s1.cpe = info[tcp_port]['cpe']
            s1.extrainfo = info[tcp_port]['extrainfo']
            s1.update_time = info['update_time']
            s1.save()
