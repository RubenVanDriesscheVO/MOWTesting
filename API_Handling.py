import requests
import configparser
import json

url = "https://digitaalarchief-ti.vlaanderen.be/auth/ropc.php"


def get_token(config_file):
    """
    Haalt een token op om aan te melden op de api op basis van de gegevens in een ini file
    """
    #Uitlezen INI file
    configreader = configparser.ConfigParser()
    configreader.read(config_file)
    client_id = configreader["USER_TI"]["client_id"]
    client_secret = configreader["USER_TI"]["client_secret"]
    username = configreader["USER_TI"]["username"]
    password = configreader["USER_TI"]["password"]
    #payload klaarmaken
    header = {
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
    'grant_type': password,
    'username': username,
    'password': password,
    'scope': 'read:sample',
    'client_id': client_id,
    'client_secret': client_secret
    }
    #request versturen
    response = requests.post(url, headers=header, data=data)
    if response.status_code == 200:
        print("Connectie gelukt")
        answer = response.json()
        return answer
    else:
        raise Exception("Connectie niet gelukt: ", response.status_code, response.text)


def send_representation(token, representationid, file_path):
    """
    Verstuur representaties naar het edepot.
    """
    header = {
        'Authorization': f'Bearer {token}',
    }
    data = {}
    with open(file_path, 'rb') as file_open:
        files={
            'file': file_open
        }
        print(files)
        response = requests.post(f'https://digitaalarchief-ti.vlaanderen.be/edepot/api/v1/records/:{representationid}/digitize', headers=header, files=files, data=data)
    if response.status_code == 201:
        print("Bestand succesvol opgeladen!")
    else:
        raise Exception("Bestand opladen niet gelukt: ", response.status_code, response.text)
    


if __name__ == "__main__":
    get_token('config.ini')    