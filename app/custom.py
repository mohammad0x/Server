from .zoho import *
from django.http import HttpResponse
from .lightspeed import *

url_light = "https://cloud.lightspeedapp.com/oauth/access_token.php"
client_id_light = "*********************************"
client_secret_light = "***********************************"

url_zoho = 'https://accounts.zoho.com/oauth/v2/token'
client_id_zoho = '1000.*************************'
client_secret_zoho = '***************'
refresh_token = '1000.*********.***************'

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
