import requests
import json 
import pytest
from data_providers import read_json_data, read_excel_data, read_csv_data
import csv

BASE_URL = "http://simple-books-api.click/orders"
AUTH_TOKEN = "cad558ed7b7e28ec29f4878ce42af05d039c2368aefc02f1cad2d12d3d3cb0ce"

def submit_delete_order(book_id,customer_name):
    payload = {
        "bookId": int(book_id),
        "customerName": customer_name
    }

    headers = {
        "Authorization": AUTH_TOKEN,
        "Content-Type": "application/json"
    }
    res = requests.post(BASE_URL, headers=headers, data=json.dumps(payload))

    assert res.status_code == 201, "wrong status code"
    order_id = res.json()["orderId"]
    print("Order Submitted with orderid = ", order_id)

    #Delete order 
    del_res = requests.delete(f"{BASE_URL}/{order_id}", headers=headers)
    assert del_res.status_code == 204, "Order not deleted"
    print("Order Deleted")

@pytest.mark.parametrize('order_data',read_json_data(r"C:\development\Studying\API\Day9\testdata\orders_json_data.json"))
def test_with_json_data(order_data):
    order_data = order_data[0]
    submit_delete_order(order_data["BookID"], order_data["CustomerName"])

@pytest.mark.parametrize('book_id, customer_name', read_csv_data(r"C:\development\Studying\API\Day9\testdata\orders_csv_data.csv"))
def test_with_csv_data(book_id,customer_name):
    submit_delete_order(book_id,customer_name)

@pytest.mark.parametrize('book_id, customer_name', read_excel_data(r"C:\development\Studying\API\Day9\testdata\orders_excel_data.xlsx"))
def test_with_excel_data(book_id,customer_name):
    submit_delete_order(book_id,customer_name)

