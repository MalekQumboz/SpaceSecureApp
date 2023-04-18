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

    context.mainservices = service_list
    context.packages = package_list

    frappe.db.commit()

    return context
