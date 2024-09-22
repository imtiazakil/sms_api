from django.db import models

# Create your models here.
class SMSLog(models.Model):
    mobile_no = models.CharField(max_length=15)
    sms_body = models.TextField()
    response_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SMS to {self.mobile_no}"