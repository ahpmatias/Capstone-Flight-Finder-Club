import os
import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.tequila_data = None
        self.tequila_get_response = None
        self.tequila_api_key = '2dYgu4BLhNHlrcHuIPt2rb7JBTtSrW_v'
        self.tequila_endpoint = 'https://api.tequila.kiwi.com/locations/query'

    def get_data(self, params, headers):
        self.tequila_get_response = requests.get(url= self.tequila_endpoint,
                                                 params=params, headers=headers)
        self.tequila_data = self.tequila_get_response.json()

        return self.tequila_data

    def location_query(self):
        pass

