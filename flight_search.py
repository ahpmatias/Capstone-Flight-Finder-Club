import os
import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.tequila_get_price_data = None
        self.tequila_get_price_response = None
        self.tequila_data = None
        self.tequila_get_response = None
        self.tequila_api_key = '2dYgu4BLhNHlrcHuIPt2rb7JBTtSrW_v'
        self.tequila_locations_endpoint = 'https://api.tequila.kiwi.com/locations/query'
        self.tequila_search_endpoint = 'https://api.tequila.kiwi.com/search'

    def get_data(self, params, headers):
        self.tequila_get_response = requests.get(url=self.tequila_locations_endpoint,
                                                 params=params, headers=headers)
        self.tequila_data = self.tequila_get_response.json()

        return self.tequila_data

    def get_flights_data(self, params, headers):
        self.tequila_get_price_response = requests.get(url=self.tequila_search_endpoint,
                                                       params=params, headers=headers)
        self.tequila_get_price_data = self.tequila_get_price_response.json()

        return self.tequila_get_price_data

