from http import HTTPStatus
from datetime import timedelta, datetime
from rest_framework.views import APIView
from response import CustomResponse, ERROR_CODES
#假设其他组的模型表已经建好
from abnormal_attack.models import AbnormalTraffic,AbnormalHost,AbnormalUser

class ThreatAPIView(APIView):
    def getAbnormalTrafficCount(self, current_date):
        counts = {}
        for attack_type in AbnormalTraffic.FLOW_TYPE_CHOICES:
            count = AbnormalTraffic.objects.filter(time__date=current_date, type=attack_type[0]).count()
            counts[attack_type[1]] = count
        return counts

    def getAbnormalUserCount(self, current_date):
        count = AbnormalUser.objects.filter(time__date=current_date,type=1).count()
        return {'异常用户': count}

    def getAbnormalHostCount(self, current_date):
        count = AbnormalHost.objects.filter(time__date=current_date).count()
        return {'异常主机': count}

    def get(self, request):
        try:
            # 获取当前日期和7天前的日期
            end_date = datetime.now().date()
            start_date = end_date - timedelta(days=6)

            # 查询每一天每种攻击类型的数量
            attack_type_counts = {
                'DDoS': [],
                'Webshell': [],
                'Botnet': [],
                'Trojan': [],
                'Worm': [],
                'Virus': [],
                'SQL Injection': [],
                'XML Injection': [],
                'XSS': [],
                'Port Scan': [],
                '异常用户': [],
                '异常主机': []
            }

            total_counts = {}

            current_date = start_date
            while current_date <= end_date:
                for method in [self.getAbnormalTrafficCount, self.getAbnormalUserCount, self.getAbnormalHostCount]:
                    counts = method(current_date)
                    for attack_type, count in counts.items():
                         attack_type_counts[attack_type].append(count)
                         total_counts[attack_type] = total_counts.get(attack_type, 0) + count

                current_date += timedelta(days=1)

             # 计算每种攻击类型占所有攻击类型的百分比
            total_count_sum = sum(total_counts.values())
            if total_count_sum != 0:
                for attack_type, count in total_counts.items():
                    total_counts[attack_type] = {
                        'count': count,
                        'percentage': round(count / total_count_sum * 100, 2)
                    }
            else:
                for attack_type, count in total_counts.items():
                    total_counts[attack_type] = {
                        'count': count,
                        'percentage': 0
                    }

            return CustomResponse(data={
                'attack_type_counts':attack_type_counts,
                'total_counts':total_counts,
                })
        except Exception as e:
            return CustomResponse(
                code=ERROR_CODES['INTERNAL_SERVER_ERROR'],
                msg=str(e),
                data=[],
                status=HTTPStatus.INTERNAL_SERVER_ERROR
            )