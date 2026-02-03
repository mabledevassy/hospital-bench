# Copyright (c) 2026, Mable Devassy and contributors
# For license information, please see license.txt

import frappe



def execute(filters=None):
    columns = [
        {"label": "Appointment ID", "fieldname": "name", "fieldtype": "Link", "options": "Appointment", "width": 150},
        {"label": "Doctor", "fieldname": "doctor_name", "width": 180},
        {"label": "Date", "fieldname": "appointment_date", "fieldtype": "Date", "width": 120},
        {"label": "From Time", "fieldname": "from_time", "width": 100},
        {"label": "To Time", "fieldname": "to_time", "width": 100},
        {"label": "Status", "fieldname": "status", "width": 120}
    ]

    data = []

    appointments = frappe.get_all(
        "Appointment",
        filters={"patient": filters.get("patient")},
        fields=["name", "doctor", "appointment_date", "from_time", "to_time", "status"],
        order_by="appointment_date desc"
    )

    for appt in appointments:
        data.append({
            "name": appt.name,
            "doctor_name": frappe.db.get_value("Doctor", appt.doctor, "doctor_name"),
            "appointment_date": appt.appointment_date,
            "from_time": appt.from_time,
            "to_time": appt.to_time,
            "status": appt.status
        })

    return columns, data


