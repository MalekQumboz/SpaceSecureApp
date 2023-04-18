import frappe


def get_context(context):
    package = frappe.db.get_all("Package", {"active": 1})
    service = frappe.db.get_all("Main Service")

    package_list = []
    service_list = []


    for val in package:
        data = frappe.get_doc("Package", val["name"])
        package_list.append(data)

    for val in service:
        data = frappe.get_doc("Main Service", val["name"])
        service_list.append(data)

    frappe.db.commit()

    context.mainservices = service_list
    context.packages = package_list

    return context


@frappe.whitelist(True)
def insert_data(full_name,email,phone,description,type,srevice_name="",
                package_name="",complaint_topic="",technical_support=""):
    type_message=""
    if type:
        if type =="srev":
            type_message="طلب خدمة"
        elif type =="grievance":
            type_message="تقديم شكوى"
        elif type == "sugg":
            type_message = "الدعم الفني"


    doc = frappe.get_doc({
        "doctype": "Communication Requests",
        "full_name": full_name,
        "email": email,
        "phone": phone,
        "type": type_message,
        "srevice_name": srevice_name,
        "package_name": package_name,
        "complaint_topic": complaint_topic,
        "technical_support": technical_support,
        "description":description

    })
    doc.insert(ignore_permissions=True)
    frappe.db.commit()