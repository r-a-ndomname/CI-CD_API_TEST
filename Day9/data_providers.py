import json 
import csv 
import os
from openpyxl import load_workbook
BASE = os.path.dirname(__file__)
# JSON Data Provider
def read_json_data(filepath):
    with open(os.path.join(BASE, filepath), "r") as f:
        data_list = json.load(f)
    return [(item,) for item in data_list]
# CSV Data Provider 
def read_csv_data(filepath):
    data_list = []
    with open(os.path.join(BASE, filepath), "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            data_list.append(tuple(row))
    return data_list 
def read_excel_data(filepath):
    data_list = []
    workbook = load_workbook(os.path.join(BASE, filepath), read_only=True, data_only=True)
    sheet = workbook.active
    rows = sheet.iter_rows(values_only=True)
    next(rows)
    for row in rows:
        if row and row[0] is not None: 
            data_list.append(row)
    workbook.close() 
    return data_list