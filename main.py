# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from flight_data import FlightData

sheety = DataManager()
tequila1 = FlightSearch()
tequila2 = FlightData

sheety.get_sheety_data()

tequila_header = {
    "Content-Type": "application/json",
    'apikey': tequila1.tequila_api_key
}

sheety.update_iata_codes(tequila_header, tequila1)

today = datetime.now()

search_params = {
    'fly_from': 'LON',
    'fly_to': 'PAR',
    'date_from': (today + timedelta(1)).strftime('%d/%m/%Y'),
    'date_to': (today + timedelta(180)).strftime('%d/%m/%Y'),
    'nights_in_dst_from': 7,
    'nights_in_dst_to': 28,
    'curr': 'GBP',
    'max_stopovers': 0,
}

for num in range(0, len(sheety.cities)):
    search_params = {
        'fly_from': 'LON',
        'fly_to': sheety.cities[num],
        'date_from': (today + timedelta(1)).strftime('%d/%m/%Y'),
        'date_to': (today + timedelta(180)).strftime('%d/%m/%Y'),
        'nights_in_dst_from': 7,
        'nights_in_dst_to': 28,
        'curr': 'GBP',
        'max_stopovers': 0,
    }
    flights_data = tequila1.get_flights_data(params=search_params, headers=tequila_header)
    min_price = tequila2.get_min_price_data(flights_data)
    city_to = flights_data['data'][0]['cityTo']
    print(f'{city_to}: ${min_price}')
