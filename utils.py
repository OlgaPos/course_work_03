import requests
from pprint import pprint


def get_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json(), "Данные получены успешно"
        return None, f"status_code: {response.status_code}"
    except requests.exceptions.ConnectionError:
        return None, "ConnectionError"
    except requests.exceptions.ConnectTimeout:
        return None, "ConnectTimeout"
    except requests.exceptions.JSONDecodeError:
        return None, "JSONDecodeError"



#