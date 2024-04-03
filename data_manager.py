import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.sheety_get_response = None
        self.city_list = None
        self.sheety_data = None
        self.sheety_user = 'ahpmatias'
        self.sheety_password = 'capstoneday40'
        self.sheety_endpoint = 'https://api.sheety.co/eff378423459742ece3e9cb2e57e9dd5/flightDeals/prices'

    def get_data(self):
        self.sheety_get_response = requests.get(url=self.sheety_endpoint)
        self.sheety_data = self.sheety_get_response.json()
        
        return self.sheety_data

    def get_city_list(self):
        
        self.city_list = []

        for city in range(0, len(self.sheety_data['prices'])):
            self.city_list.append(self.sheety_data['prices'][city]['city'])

        return self.city_list
