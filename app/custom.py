from .zoho import *
from django.http import HttpResponse
from .lightspeed import *

url_light = "https://cloud.lightspeedapp.com/oauth/access_token.php"
client_id_light = "83bec51c4baccc96a28a7f7ca353acc8246c66dee16f24d3a186b0af079dbdcb"
client_secret_light = "2ac17e023778d1fa56b68dc9a9065b0b165a6788484e8a0bcf75e95d22311451"

url_zoho = 'https://accounts.zoho.com/oauth/v2/token'
client_id_zoho = '1000.GJIMCDUESNK18PS1SH8XK4XL6MF2FF'
client_secret_zoho = '1e8274522ba8d68f2598828cd50cfc471c9ea879f3'
refresh_token = '1000.4de57c2028639b91c64bba71ed0357c0.c5bd35b7e5791620fe352b5c50fe1c7f'

conn = http.client.HTTPSConnection("www.zohoapis.com")

def getItem(access_token, zoho_access_token, item_id):
    light_url = f'https://api.lightspeedapp.com/API/V3/Account/292471/Item/{item_id}.json?load_relations=all&sort=itemID&limit=100&after=WzExMzI1XQ%3D%3D'

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
        dic = {
            'name': result['Item']['description'],
            'qty': result['Item']['ItemShops']['ItemShop'][0]['qoh'],
            'cost': result['Item']['defaultCost'],
            'price': result['Item']['Prices']['ItemPrice'][0]['amount']
        }

        readData(zoho_access_token, dic)
        return result
    except:
        return HttpResponse('getListItem error')