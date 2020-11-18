from django.shortcuts import render

# App imports
from .models import Message
from .serializers import MessageSerializer
# Create your views here.

# rest framework serializers
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response


class MessageListApiView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageCreateApiView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class OutboxListApiView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(sender=user)


class DeleteMessageApiView(generics.DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_destroy(self, instance):
        current_user = self.request.user
        sender = instance.sender
        if current_user != sender:
            return Response({'message': 'You are not permitted to delete this message.'}, status=status.HTTP_403_FORBIDDEN)
        else:
            instance.delete()


class InboxListApiView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(reciever=user)