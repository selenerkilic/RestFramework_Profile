import requests
from pprint import pprint 
def client():
    credentials = {
        'username' : 'test_user',
        'password' : '12345test',
    }
     
    response = requests.post(
        url='http://127.0.0.1:8000/api/rest-auth/login/', 
        data=credentials,
    )

    print('Status Code:', response.status_code)

    response_data = response.json()
    pprint(response_data)

if __name__ == '__main__':
    client()