import requests
import json 

class TestOrderAPI:
    BASE_URL = "http://simple-books-api.click/orders"
    AUTH_TOKEN = "cad558ed7b7e28ec29f4878ce42af05d039c2368aefc02f1cad2d12d3d3cb0ce"

    def test_submit_delete_order(self):
        payload = {
            "bookId": 1,
            "customerName": "John"
        }

        headers = {
            "Authorization": self.AUTH_TOKEN,
            "Content-Type": "application/json"
        }
        res = requests.post(self.BASE_URL, headers=headers, data=json.dumps(payload))

        assert res.status_code == 201, "wrong status code"
        order_id = res.json()["orderId"]
        print("Order Submitted with orderid = ", order_id)

        #Delete order 
        del_res = requests.delete(f"{self.BASE_URL}/{order_id}", headers=headers)
        assert del_res.status_code == 204, "Order not deleted"
        print("Order Deleted")


