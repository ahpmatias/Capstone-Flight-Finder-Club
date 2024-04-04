import requests
import os


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.sheety_get_response = None
        self.city_list = None
        self.sheety_data = None
        self.sheety_user = os.environ.get('SHEETY_USER')
        self.sheety_password = os.environ.get('SHEETY_PASSWORD')
        sheety_id = os.environ.get('SHEETY_ID')
        self.sheety_endpoint = f'https://api.sheety.co/{sheety_id}/flightDeals/prices'
        self.cities = self.get_city_list()
    def get_sheety_data(self):
        self.sheety_get_response = requests.get(url=self.sheety_endpoint)
        self.sheety_data = self.sheety_get_response.json()

        return self.sheety_data

    def get_city_list(self):

        self.city_list = []

        for city in range(0, len(self.sheety_data['prices'])):
            self.city_list.append(self.sheety_data['prices'][city]['city'])

        return self.city_list

    def update_iata_codes(self, tequila_header, tequila):

        for num in range(0, len(self.cities)):
            tequila_params = {
                'term': self.cities[num]
            }
            tequila_data = tequila.get_sheety_data(tequila_params, tequila_header)
            current_city = tequila_data['locations'][0]['code']
            sheety_update = {
                'price': {
                    'code': current_city
                }
            }
            requests.put(url=f'{self.sheety_endpoint}/{num + 2}', json=sheety_update,
                         auth=(self.sheety_user, self.sheety_password))
