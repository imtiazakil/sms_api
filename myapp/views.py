import requests
from django.shortcuts import render, redirect
from .models import SMSLog
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.

def send_sms(request):
    if request.method == "POST":
        mobile_no = request.POST.get('mobile_no')
        sms_body = request.POST.get('sms_body')

        # API endpoint and headers
        url = "https://sysadmin.muthobarta.com/api/v1/send-sms"
        headers = {
            "Authorization": "Token ",  # Replace with your actual API Key
            "Content-Type": "application/json"
        }

        # Payload for the API request
        payload = {
            "sender_id": "",  # Replace with your sender ID
            "receiver": mobile_no,
            "message": sms_body,
            "remove_duplicate": True
        }

        try:
            # Sending the SMS through the API
            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()

            # Save form data and API response to the database
            SMSLog.objects.create(
                mobile_no=mobile_no,
                sms_body=sms_body,
                response_data=str(response_data)  # Convert response to string for saving
            )

            # Redirect or render success page
            messages.success(request, "SMS successfully sent to all numbers!")
            return redirect(request.path)

        except requests.exceptions.RequestException as e:
            return JsonResponse({"error": str(e)})

    return render(request, 'sms.html')

def sms_log(request):
    sms_logs = SMSLog.objects.all().order_by('-created_at')
    return render(request, 'sms_data.html', {'sms_logs': sms_logs})