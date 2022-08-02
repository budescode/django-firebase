from rest_framework import serializers

class TodoSerializer(serializers.Serializer):    
    name = serializers.CharField()
    description = serializers.CharField()
