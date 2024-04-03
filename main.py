# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

import requests
from data_manager import DataManager
from flight_search import FlightSearch

sheety = DataManager()
tequila = FlightSearch()

sheety.get_data()

tequila_header = {
    "Content-Type": "application/json",
    'apikey': tequila.tequila_api_key
}

sheety.update_iata_codes(tequila_header, tequila)
