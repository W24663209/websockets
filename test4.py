import requests

response = requests.post(url='https://webhook.kingpay.io/api/kes/sms?text=SGB7B9W0B9%20Confirmed.%20Ksh1.00%20sent%20to%20Aileen%20%20mwanja%200706084180%20on%2011/7/24%20at%2012:19%20PM.%20New%20M-PESA%20balance%20is%20Ksh346.62.%20Transaction%20cost,%20Ksh0.00.%20Amoun&ANDROID_ID=6876e02ecbb56ec1", "headers": "python-requests/2.31.0", "client_ip": "172.71.218.52", "request_params": "text=SGB7B9W0B9%20Confirmed.%20Ksh1.00%20sent%20to%20Aileen%20%20mwanja%200706084180%20on%2011/7/24%20at%2012:19%20PM.%20New%20M-PESA%20balance%20is%20Ksh346.62.%20Transaction%20cost,%20Ksh0.00.%20Amoun&ANDROID_ID=6876e02ecbb56ec1')
print(response.json())
