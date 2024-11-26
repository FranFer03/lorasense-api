from rest_framework import serializers
from sensor_gateway.models import *

class NodeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = NodeData
        fields = '__all__'
