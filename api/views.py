from django.shortcuts import render
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from message.models import Message
from .serializers import MessageSerializer
# Create your views here.

class MessageList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        token = self.request.META.get('HTTP_AUTHORIZATION').split()[1]
        user = Token.objects.get(key=token).user
        serializer.save(created_by=user)
