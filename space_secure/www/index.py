import frappe
def get_context(context):
	context.host_package = frappe.get_last_doc("Package",filters={"active":1,"main_service": "خدمة الاستضافة"})
	context.cypersecurity_package = frappe.get_last_doc("Package",filters={"active":1,"main_service":"خدمة الامن السيبراني"})
	context.webservice_package = frappe.get_last_doc("Package",filters={"active":1,"main_service": "خدمة تصميم المواقع والتطبيقات"})
	webservice_2 = frappe.db.get_all("Package",{"active":1,"main_service": "خدمة تصميم المواقع والتطبيقات"})
	context.webservice_package_2=frappe.get_doc("Package",webservice_2[1]["name"])

	return context




@frappe.whitelist(True)
def insert_data(full_name,email,phone,description):

    doc = frappe.get_doc({
        "doctype": "Communication Requests",
        "full_name": full_name,
        "email": email,
        "phone": phone,
		"description":description,
        "type":"طلب خدمة"
    })
    doc.insert(ignore_permissions=True)
    frappe.db.commit()
