import frappe
def get_context(context):
	context.host_package = frappe.get_last_doc("Package", filters={"active": 1, "main_service": "خدمة الاستضافة"})
	context.cypersecurity_package = frappe.get_last_doc("Package",filters={"active": 1, "main_service": "خدمة الامن السيبراني"})
	context.webservice_package = frappe.get_last_doc("Package", filters={"active": 1,"main_service": "خدمة تصميم المواقع والتطبيقات"})
	webservice_2 = frappe.db.get_all("Package", {"active": 1, "main_service": "خدمة تصميم المواقع والتطبيقات"})
	context.webservice_package_2 = frappe.get_doc("Package", webservice_2[1]["name"])

	cypersecurity=frappe.db.get_all("Sub Service",{"active":1,"main_services_name": "خدمة الامن السيبراني"})
	host=frappe.db.get_all("Sub Service",{"active":1,"main_services_name": "خدمة الاستضافة"})
	webservice = frappe.db.get_all("Sub Service",{"active":1,"main_services_name": "خدمة تصميم المواقع والتطبيقات"})


	cypersecurity_list=[]
	host_list=[]
	webservice_list=[]

	for val in cypersecurity:
		data=frappe.get_doc("Sub Service", val["name"])
		cypersecurity_list.append(data)


	for val in host:
		data=frappe.get_doc("Sub Service", val["name"])
		host_list.append(data)

	for val in webservice:
		data=frappe.get_doc("Sub Service", val["name"])
		webservice_list.append(data)


	context.cypersecurity_sub=cypersecurity_list
	context.host_sub=host_list
	context.webservice_sub=webservice_list

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
