import requests
import json

headers = { "X-Api-Key": "4bf4b36a18d831ee7a2d5a0358e576eb", "X-Auth-Token": "6227b11c27f990a040553e1d2da64d16"}

payload = {
  'purpose': 'FIFA 16',
  'amount': '2500',
  'buyer_name': 'John Doe',
  'email': 'foo@example.com',
  'phone': '9999999999',
  'redirect_url': 'http://www.example.com/redirect/',
  'send_email': 'True',
  'send_sms': 'True',
  'webhook': 'http://www.example.com/webhook/',
  'allow_repeated_payments': 'False',
}

def create_request(amount=10):
    payload['amount'] = amount
    response = requests.post("https://www.instamojo.com/api/1.1/payment-requests/", data=payload, headers=headers)
    json_data = json.loads(response.text)
    return json_data['payment_request']['longurl']
