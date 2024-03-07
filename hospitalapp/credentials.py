import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64


class MpesaC2bCredential:
    consumer_key = 'LUMs2AQ8FRYQg8Kv5ET5SMuLkabQbElIMB5NP5jNEfeAAIAG'
    consumer_secret = 'tAuJDVmnjUy5IIpm5pdc6nBpAAdEjCRw2cscaz2YB2bJBCDm9wLJ1o94icpnfrFM'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class MpesaAccessToken:
    r = requests.get(MpesaC2bCredential.api_URL,
                     auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]


class LipanaMpesaPpassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = "174379"
    OffSetValue = '0'
    passkey = 'tAuJDVmnjUy5IIpm5pdc6nBpAAdEjCRw2cscaz2YB2bJBCDm9wLJ1o94icpnfrFM'

    data_to_encode = Business_short_code + passkey + lipa_time

    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')
