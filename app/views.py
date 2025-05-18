from django.shortcuts import render, redirect
from .lightspeed import *
from django.http import HttpResponse
from .custom import *
# Create your views here.


def run1(request):
    url_zoho = 'https://accounts.zoho.com/oauth/v2/token'
    client_id_zoho = '1000.***********************'
    client_secret_zoho = '*************************'
    refresh_token = '1000.****************.*********************'

    light_url = "https://api.lightspeedapp.com/API/V3/Account/292471/Item.json?load_relations=all"
    global zoho_access_token
    zoho_access_token = getAccessToken(client_id_zoho, client_secret_zoho, refresh_token, url_zoho)
    light_access_token = getRefreshToken()
    data2 = getListItem(light_access_token, zoho_access_token, light_url)
    time.sleep(2)
    data3 = getOtherListItem(data2[0], data2[1], zoho_access_token)


    t = 0
    for i in range(70):
        if t == 0:
            t += 1
            data4 = getOtherListItem(data3[0], data3[1],zoho_access_token)
        else:
            data4 = getOtherListItem(data4[0], data4[1],zoho_access_token)
    return HttpResponse('ok1')

def run2(request):
    url_zoho = 'https://accounts.zoho.com/oauth/v2/token'
    client_id_zoho = '1000.*******************************'
    client_secret_zoho = '*****************************'
    refresh_token = '1000.*************.*********************'

    # page 69 url
    light_url = 'https://api.lightspeedapp.com/API/V3/Account/292471/Item.json?load_relations=all&sort=itemID&limit=100&after=WzExMzI1XQ%3D%3D'
    global zoho_access_token
    zoho_access_token = getAccessToken(client_id_zoho, client_secret_zoho, refresh_token, url_zoho)
    light_access_token = getRefreshToken()
    data2 = getListItem(light_access_token, zoho_access_token, light_url)
    data3 = getOtherListItem(data2[0], data2[1], zoho_access_token)

    t = 0
    for i in range(70):
        if t == 0:
            t += 1
            data4 = getOtherListItem(data3[0], data3[1],zoho_access_token)
        else:
            data4 = getOtherListItem(data4[0], data4[1],zoho_access_token)
    return HttpResponse('ok2')

def custom(request):
    if request.method == 'POST':
        item_id = request.POST['system_id']

        url_zoho = 'https://accounts.zoho.com/oauth/v2/token'
        client_id_zoho = '1000.**************************'
        client_secret_zoho = '************************'
        refresh_token = '1000.************************.*****************************'


        global zoho_access_token
        zoho_access_token = getAccessToken(client_id_zoho, client_secret_zoho, refresh_token, url_zoho)
        light_access_token = getRefreshToken()
        getItem(light_access_token, zoho_access_token, item_id)

    return render(request, 'custom.html')
