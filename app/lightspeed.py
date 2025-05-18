import requests
import time
import http.client
import json
from .zoho import *
from django.http import HttpResponse

url_light = "https://cloud.lightspeedapp.com/oauth/access_token.php"
client_id_light = "***************************************"
client_secret_light = "**************************************"

url_zoho = 'https://accounts.zoho.com/oauth/v2/token'
client_id_zoho = '1000.********************'
client_secret_zoho = '******************************'
refresh_token = '1000.*******.***********************'

conn = http.client.HTTPSConnection("www.zohoapis.com")


def getAccessToken(client_id_zoho, client_secret_zoho, refresh_token, url_zoho):
    playload = {
        'client_id': client_id_zoho,
        'client_secret': client_secret_zoho,
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token',
        'redirect_uri': 'https://localhost'
    }
    response = requests.post(url_zoho, data=playload)
    try:
        zoho_access_token = json.loads(response.text)['access_token']
        print(zoho_access_token)
        return zoho_access_token
    except:
        return HttpResponse('getAccessToken error')

def getRefreshToken():
    payload1 = {
        "client_id": client_id_light,
        "client_secret": client_secret_light,
        "refresh_token": '347c4fae95e862669dc739bf61b9f01ea0283ebb',
        "grant_type": "refresh_token"
    }
    response = requests.post(url_light, data=payload1)
    try:
        access_token = json.loads(response.text)['access_token']
        print(access_token)
        return access_token
    except:
        return HttpResponse('getRefreshToken error')


def getListItem(access_token, zoho_access_token, light_url):
    header = {
        "authorization": f"Bearer {access_token}",
    }

    response = requests.get(light_url, headers=header)
    try:
        code = json.loads(response.text)['httpCode']
        if code == '401':
            res = getRefreshToken()
            header = {
                "authorization": f"Bearer {res}",
            }

            response = requests.get(light_url, headers=header)

    except:
        pass

    try:
        result = json.loads(response.text)
        next = json.loads(response.text)['@attributes']['next']
        for i in range(len(result['Item'])):
            time.sleep(1)
            dic = {
                'name': result['Item'][i]['description'],
                'qty': result['Item'][i]['ItemShops']['ItemShop'][0]['qoh'],
                'cost': result['Item'][i]['defaultCost'],
                'price': result['Item'][i]['Prices']['ItemPrice'][0]['amount']
            }
            readData(zoho_access_token, dic)
        print('complete')
        return next, access_token
    except:
        return HttpResponse('getListItem error')
def getOtherListItem(urlNext, access_token, zoho_access_token):
    header = {
        "authorization": f"Bearer {access_token}",
    }

    response = requests.get(urlNext, headers=header)
    try:
        code = json.loads(response.text)['httpCode']
        if code == '401':
            res = getRefreshToken()
            header = {
                "authorization": f"Bearer {res}",
            }

            response = requests.get(urlNext, headers=header)
    except:
        pass

    try:
        result = json.loads(response.text)
        next = json.loads(response.text)['@attributes']['next']
        for i in range(len(result['Item'])):
            dic = {
                'name': result['Item'][i]['description'],
                'qty': result['Item'][i]['ItemShops']['ItemShop'][0]['qoh'],
                'cost': result['Item'][i]['defaultCost']
                , 'upc': result['Item'][i]['upc'],
                'price': result['Item'][i]['Prices']['ItemPrice'][0]['amount']
            }
            time.sleep(1)
            readData(zoho_access_token, dic)
        print('complete')
        return next, access_token
    except:
        return HttpResponse('getOtherListItem error')
