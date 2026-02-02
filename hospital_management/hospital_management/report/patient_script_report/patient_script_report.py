# Copyright (c) 2026, Mable Devassy and contributors
# For license information, please see license.txt

# import frappe


# def execute(filters=None):
# 	columns, data = [], []
# 	return columns, data
import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    return [
        {"label": "Patient ID", "fieldname": "name", "fieldtype": "Link", "options": "Patient", "width": 150},
        {"label": "Patient Name", "fieldname": "patient_name", "fieldtype": "Data", "width": 200},
        {"label": "Gender", "fieldname": "gender", "fieldtype": "Data", "width": 100},
        {"label": "Age", "fieldname": "age", "fieldtype": "Int", "width": 80},
        {"label": "Phone", "fieldname": "phone", "fieldtype": "Data", "width": 150},
    ]


def get_data(filters):
    conditions = {}
    
    if filters.get("patient"):
        conditions["name"] = filters.get("patient")

    if filters.get("gender"):
        conditions["gender"] = filters.get("gender")

    return frappe.get_all(
        "Patient",
        filters=conditions,
        fields=["name", "patient_name", "gender", "age", "phone"]
    )

