from django.urls import path
from .views import (
    MessageListApiView,
    MessageCreateApiView,
    OutboxListApiView,
    InboxListApiView,
    DeleteMessageApiView
)

urlpatterns = [
    path('messages/', MessageListApiView.as_view(), name='message_list'),
    path('create-message/', MessageCreateApiView.as_view(), name='message_create'),
    path('outbox/', OutboxListApiView.as_view(), name='my_outbox'),
    path('inbox/', InboxListApiView.as_view(), name='my_inbox'),
    path('delete_msg/<pk>/', DeleteMessageApiView.as_view(), name='delete_msg'),
]