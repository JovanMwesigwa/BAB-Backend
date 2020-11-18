from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'msg_content', 'reciever', 'date_sent']
        # depth = 1



