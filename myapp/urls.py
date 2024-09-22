from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('sent-sms/',views.send_sms, name='sent-sms'),
    path('sms-log/',views.sms_log, name='sms-log'),
]