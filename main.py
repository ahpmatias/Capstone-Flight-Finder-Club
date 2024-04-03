# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

import requests
from data_manager import DataManager
from flight_search import FlightSearch

sheety = DataManager()
tequila = FlightSearch()

sheety.get_data()
sheety.get_city_list()

tequila_header = {
    'apikey': tequila.tequila_api_key
}

tequila_params = {
    'term': sheety.city_list[0]
}

tequila_data = tequila.get_data(tequila_params, tequila_header)

print(tequila_data['locations'][0]['code'])
