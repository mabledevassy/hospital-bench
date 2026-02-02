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
