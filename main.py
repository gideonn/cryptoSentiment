import requests
import requests.auth
import json

def getCredentials(fileLocation):
    with open(fileLocation, 'r') as f:
        credentials = json.load(f)

    # print(credentials)
    return credentials


def auth(filePath):
    credentials = getCredentials(filePath)
    client_auth = requests.auth.HTTPBasicAuth(credentials['appID'], credentials['appSecret'])
    post_data = {"grant_type": "password", "username": credentials['username'], "password": credentials['password']}
    headers = {"User-Agent": "Crypto/0.1 by cryptobot123"}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    print(response.json())


if __name__ == '__main__':
    auth('config1.txt')