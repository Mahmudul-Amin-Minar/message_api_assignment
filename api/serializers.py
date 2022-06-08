from rest_framework import serializers
from django.contrib.auth.models import User

from message.models import Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class MessageSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(many=False, read_only=True)

    
    class Meta:
        fields = ('id', 'message', 'created_at', 'updated_at', 'created_by')
        model = Message

    def create(self, validated_data):
        return Message.objects.create(**validated_data)
    