import requests
from pprint import pprint 

def client():
    credentials = {
        'username' : 'rest_test_user_2',
        'email' : 'test2@test.co',
        'password1' : '12345test**',
        'password2' : '12345test**',
    }
     
    response = requests.post(
        url='http://127.0.0.1:8000/api/rest-auth/registration/', 
        data=credentials,
    )

    print('Status Code:', response.status_code)

    response_data = response.json()
    pprint(response_data)

if __name__ == '__main__':
    client()