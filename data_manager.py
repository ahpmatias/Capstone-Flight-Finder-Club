import requests
from flight_search import FlightSearch


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

    def update_iata_codes(self, tequila_header, tequila):
        cities = self.get_city_list()
        for num in range(0, len(cities)):
            tequila_params = {
                'term': cities[num]
            }
            tequila_data = tequila.get_data(tequila_params, tequila_header)
            current_city = tequila_data['locations'][0]['code']
            sheety_update = {
                'price': {
                    'code': current_city
                }
            }
            print(num)
            print(current_city)
            requests.put(url=f'{self.sheety_endpoint}/{num + 2}', json=sheety_update,
                         auth=(self.sheety_user, self.sheety_password))
