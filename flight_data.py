from data_manager import DataManager
from datetime import datetime, timedelta


class FlightData:
    # This class is responsible for structuring the flight data.

    def get_min_price_data(self):
        prices = []
        for num in range(0, len(self['data'])):
            prices.append(self['data'][num]['price'])

        return min(prices)

    # def show_best_prices(self):
    #     cities = DataManager.get_city_list()
    #     today = datetime.now()
    #     for num in range(0, len(cities)):
    #         search_params = {
    #             'fly_from': 'LON',
    #             'fly_to': cities[num],
    #             'date_from': (today + timedelta(1)).strftime('%d/%m/%Y'),
    #             'date_to': (today + timedelta(180)).strftime('%d/%m/%Y'),
    #             'nights_in_dst_from': 7,
    #             'nights_in_dst_to': 28,
    #             'curr': 'GBP',
    #             'max_stopovers': 0,
    #         }
    #
    #         current_city = tequila_data['locations'][0]['code']
    #         sheety_update = {
    #             'price': {
    #                 'code': current_city
    #             }
    #         }
