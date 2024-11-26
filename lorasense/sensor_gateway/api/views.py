from rest_framework.response import Response
from rest_framework.views import APIView
from sensor_gateway.models import *
from sensor_gateway.api.serializers import *

class SensorData(APIView):
    def get(self,request):
        platform = NodeData.objects.all()
        serializer = NodeDataSerializer(platform,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = NodeDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
