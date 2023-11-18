# from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from asset_management.models import Workshop
from asset_management.serializers import WorkshopSerializer
from rest_framework.response import Response


class WorkshopBasicView(APIView):

    def get(self, request):
        query = request.query_params.dict()
        page = int(query['page'])
        pageSize = int(query['pageSize'])
        content = str(query['content'])
        resall = Workshop.objects.all()
        reschosen = []
        for i in resall:
            if ((str(i.id).find(content) != -1)
                    or (i.name.find(content) != -1)
                    or (i.shortened.find(content) != -1)
                    or (str(i.productionline_number).find(content) != -1)):
                reschosen.append(i)
        res = reschosen[(page - 1) * pageSize: page * pageSize]
        print(res)
        ser = WorkshopSerializer(instance=res, many=True)
        return Response(ser.data)

    def post(self, request):
        workshop_toadd = WorkshopSerializer(data=request.data)
        if not workshop_toadd.is_valid():
            return Response(workshop_toadd.errors)
        workshop_toadd.save()
        return Response(workshop_toadd.data)

    def put(self, request):
        query = request.query_params.dict()
        pick = int(query['alternum'])
        workshop_chosen = Workshop.objects.get(pk=pick)
        ser = WorkshopSerializer(instance=workshop_chosen, data=request.data)
        if not ser.is_valid():
            return Response(ser.errors)
        ser.save()
        return Response(ser.data)

    def delete(self, request):
        query = request.query_params.dict()
        pick = int(query['deletenum'])
        Workshop.objects.get(pk=pick).delete()
        return Response({'detail': 'Deleted successfully!'})
