from django.urls import path
from .views import send_notification

app_name = "whatsapp"

urlpatterns = [
     path('', send_notification, name="contact"),
]