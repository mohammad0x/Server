import requests
import time
import http.client
import json
from .lightspeed import *
from django.http import HttpResponse

url_zoho = 'https://accounts.zoho.com/oauth/v2/token'
client_id_zoho = '1000.GJIMCDUESNK18PS1SH8XK4XL6MF2FF'
client_secret_zoho = '1e8274522ba8d68f2598828cd50cfc471c9ea879f3'
refresh_token = '1000.4de57c2028639b91c64bba71ed0357c0.c5bd35b7e5791620fe352b5c50fe1c7f'

conn = http.client.HTTPSConnection("www.zohoapis.com")


def readData(access_token, item):
    authoriation = f"Zoho-oauthtoken {access_token}"
    headers = {
        'Authorization': authoriation,
    }

    item_name = item["name"]
    api_request = f"https://www.zohoapis.com/books/v3/items?organization_id=762023225&name={item_name}"
    res =requests.get(api_request, headers=headers)
    try:
        result = json.loads(res.text)
        print('result1')
        print(result)
        print('result2')
        code = result["code"]
        if code == 57:
            access_token = getAccessToken(refresh_token, url_zoho)
            authoriation = f"Zoho-oauthtoken {access_token}"
            headers = {
                'Authorization': authoriation
            }
            api_request = f"/books/v3/items?organization_id=762023225&name={item_name}"
            conn.request("GET", api_request, headers=headers)
            res = conn.getresponse()
            data = res.read().decode("utf-8")
            result = json.loads(data)
        if result["items"] == []:
            createItem(item["name"], float(item["cost"]), int(item["qty"]), float(item["price"]), access_token)
        else:
            defaultCost = float(item["cost"])
            qty = int(item["qty"])
            rate = float(item["price"])

            if defaultCost <= 0:
                defaultCost = 1
            if qty < 1:
                qty = 1

            res = result["items"][0]
            item_id = res["item_id"]

            if res["purchase_rate"] != defaultCost or res["stock_on_hand"] != qty or rate != res["rate"]:
                update(item_id, access_token, defaultCost, qty, rate)
    except:
        pass

def update(item_id, access_token_update, defaultCost, qty, rate):
    payload = {
        "purchase_rate": defaultCost,
        "initial_stock_rate": defaultCost,
        "initial_stock": qty,
        "rate": rate,
    }

    data = json.dumps(payload)

    authoriation_update = f"Zoho-oauthtoken {access_token_update}"
    headers = {
        'Authorization': authoriation_update,
        'content-type': "application/json"
    }

    put_api_url = f"/books/v3/items/{item_id}?organization_id=762023225"
    conn.request("PUT", put_api_url, data, headers)

    res = conn.getresponse()
    data = res.read()
    print(data)
    return HttpResponse(data)

def createItem(name, defaultCost, qty, rate, access_token):

    if defaultCost <= 0:
        defaultCost = 1
    if qty == 0:
        qty = 1

    playload = {
        "name": name,
        "item_type": "inventory",
        "purchase_rate": defaultCost,
        "initial_stock_rate": defaultCost,
        "initial_stock": qty,
        "rate": rate,
        "reorder_level": 10,
    }
    url = 'https://www.zohoapis.com/books/v3/items?organization_id=762023225'
    data = json.dumps(playload)


    authoriation_create = f"Zoho-oauthtoken {access_token}"
    headers = {
        'Authorization': authoriation_create,
        'content-type': "application/json"
    }

    try:
        response = requests.post(url, data=data, headers=headers)
        print(response.text)
        return HttpResponse(response.text)
    except:
        pass