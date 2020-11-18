from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='message_from', on_delete=models.CASCADE, null=True, blank=True)
    msg_content = models.TextField()
    reciever = models.ForeignKey(User, related_name='message_to', on_delete=models.CASCADE, null=True, blank=True)
    date_sent = models.DateTimeField(auto_now_add=True, )

    def __str__(self):
        return 'Message from {} to {}'.format(self.sender, self.reciever)