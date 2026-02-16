# import frappe
# @frappe.whitelist()
# def create_medical_record(doc, method):
#     medical = frappe.get_doc({
#         "doctype": "Medical Record",
#         "patient": doc.patient,
#         "appointment": doc.name,
#         "doctor": doc.doctor,
#         "visit_date": doc.appointment_date,
#         "items": [{
#             "diagnosis": "",
#             "prescription": "",
#             "notes": ""
#         }]
#     })
#     medical.insert(ignore_permissions=True)

import frappe
from frappe import _
from frappe.utils import nowdate, nowtime



def create_medical_record(doc, method):
    # Do NOT create medical record if appointment is cancelled
    if doc.status == "Cancelled" or doc.docstatus == 2:
        return

    # Allow only Scheduled or Completed
    if doc.status not in ["Scheduled", "Completed"]:
        return

    # Prevent duplicate medical records
    if frappe.db.exists("Medical Record", {"appointment": doc.name}):
        return

    medical = frappe.get_doc({
        "doctype": "Medical Record",
        "patient": doc.patient,
        "appointment": doc.name,
        "doctor": doc.doctor,
        "visit_date": doc.appointment_date,
        "items": [{
            "diagnosis": "",
            "prescription": "",
            "notes": ""
        }]
    })
    medical.insert(ignore_permissions=True)
    patient_name = frappe.db.get_value(
    "Patient",
    doc.patient,
    "patient_name"
    )

    frappe.msgprint(
    _("{}'s Medical Record is created successfully").format(patient_name),
    indicator="green",
    title="Medical Record Created"
    )   




@frappe.whitelist(allow_guest=False)
def get_patient_appointments(patient):
    return frappe.get_all(
        "Appointment",
        filters={"patient": patient},
        fields=[
            "name",
            "doctor",
            "appointment_date",
            "from_time",
            "to_time",
            "status"
        ],
        order_by="appointment_date desc"
    )







# def auto_complete_appointments():
#     today = nowdate()
#     current_time = nowtime()

#     appointments = frappe.get_all(
#         "Appointment",
#         filters={
#             "status": "Scheduled",
#             "appointment_date": ["<=", today]
#         },
#         fields=["name", "appointment_date", "to_time"]
#     )

#     for appt in appointments:
#         if appt.appointment_date < today or current_time > appt.to_time:
#             frappe.db.set_value(
#                 "Appointment",
#                 appt.name,
#                 "status",
#                 "Completed"
#             )
