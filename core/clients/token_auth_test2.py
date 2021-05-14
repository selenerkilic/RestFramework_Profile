import requests
from pprint import pprint 



def client():
    token = 'Token 29bf607a0b7ffbf3be50dc23503728605a7d0904' 

    headers = {
        'Authorization' : token
    }


    response = requests.get(
        url='http://localhost:8000/api/kullanici-profilleri/',
        headers = headers
    )

    print('Status Code:', response.status_code)

    response_data = response.json()
    pprint(response_data)

if __name__ == '__main__':
    client()