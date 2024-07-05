import requests
import configuration
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_URL,
                         json=body,
                         headers=data.headers)
def create_authToken():
    response = post_new_user(data.user_body)
    return response.json()["authToken"]

def post_new_client_kit(kit_body):
    auth_token = create_authToken()
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_URL,
                         json=kit_body,
                         headers=headers)
    return response



