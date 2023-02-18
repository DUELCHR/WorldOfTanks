from dictor import dictor
import requests


class ApiHelper:
    def getJsonFromUrl(api_url):
        response = requests.get(api_url)
        return response.json()
