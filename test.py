from flight_search import FlightSearch
from datetime import datetime, timedelta
from flight_data import FlightData




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

flights_data = tequila_1.get_flights_data(params=search_params, headers=tequila_header)
tequila_2.get_min_price_data(flights_data)
print(flights_data['data'][0]['cityTo'])

for num in range(0, len(cities)):
    search_params = {
        'fly_from': 'LON',
        'fly_to': cities[num],
        'date_from': (today + timedelta(1)).strftime('%d/%m/%Y'),
        'date_to': (today + timedelta(180)).strftime('%d/%m/%Y'),
        'nights_in_dst_from': 7,
        'nights_in_dst_to': 28,
        'curr': 'GBP',
        'max_stopovers': 0,
    }
