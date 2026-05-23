import json 
from pathlib import Path

import pytest  

DAY6_DIR = Path(__file__).resolve().parent

@pytest.fixture(autouse=True)
def load_json_fixture(request):
    with open(DAY6_DIR / "complex.json", "r", encoding="utf-8") as file:
        request.cls.json_response = json.load(file)


class TestParseComplexJSONResponse:
    def test_user_details_validation(self):
        #verify status
        assert self.json_response["status"] == "success", "Wrong status code"
        
        #validate userdetails
        user_details = self.json_response["data"]["userDetails"]
        assert user_details['id'] == 12345, "wrong userid"
        assert user_details['name'] == 'John Doe', "wrong name"
        assert user_details['email'] == 'john.doe@example.com', "wrong name"

        #validate Home Phone Number
        home_phone = user_details["phoneNumbers"][0]
        assert home_phone['type'] == 'home','wrong Type'
        assert home_phone['number'] == '123-456-7890','wrong number'

        #validate Geo Coordinates
        geo = user_details['address']['geo']
        assert geo['latitude'] == 39.7817, "Wrong Latitude"
        assert geo['longitude'] == -89.6501, "Wrong Longitude"

        #validate preferences 
        preferences = user_details['preferences']
        assert preferences['notifications'] is True, 'Expected notifications to be True'
        assert preferences ['theme'] == 'dark', "Wrong Theme"


    def test_recent_orders_validation(self):
        recent_orders = self.json_response['data']['recentorders']

        #verify total number of orders
        assert len(recent_orders) == 2, "Expected only 2 orders"

        #validate first order details
        first_order = recent_orders[0]
        assert first_order["orderId"] == 101, "Order Mismatch"
        assert first_order["totalAmount"] == 1226.49, "Total Amount Mismatch"

        items = recent_orders[0]['items']
        assert items[1]['name'] == 'Mouse', 'Item name mismatch'

        #Validate Second order details
        second_order = recent_orders[1]
        assert len(second_order['items']) == 1, 'Items count mismatch'
        
        # Получаем первый товар из списка товаров второго заказа
        second_order_item = second_order['items'][0] 
        
        # Проверяем данные самого ТОВАРА, а не заказа
        assert second_order_item['name'] == 'Smartphone', 'Item name mismatch'
        assert second_order_item['price'] == 799.99, 'price mismatch'

    def test_preferences_and_metadata_validation(self):
        #Validate preferences
        preferences = self.json_response['data']['userDetails']['preferences']
        languages = preferences['languages']
        assert len(languages) == 3 
        assert languages[0] == 'English'
        assert languages[1] == 'Spanish'
        assert languages[2] == 'French'

        #Validate Metadata
        metadata = self.json_response['meta']
        assert metadata['requestId'] == 'abc123xyz'
        assert metadata['responseTimeMs'] == 250

