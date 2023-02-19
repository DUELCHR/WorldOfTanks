import requests

class ApiHelper:
    def getJsonFromUrl(self, api_url):
        response = requests.get(api_url)
        return response.json()
