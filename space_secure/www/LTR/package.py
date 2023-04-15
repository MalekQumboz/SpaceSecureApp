import frappe
def get_context(context):
	cypersecurity=frappe.db.get_all("Package",{"active":1,"main_service": "خدمة الامن السيبراني"})
	host=frappe.db.get_all("Package",{"active":1,"main_service": "خدمة الاستضافة"})
	webservice = frappe.db.get_all("Package",{"active":1,"main_service": "خدمة تصميم المواقع والتطبيقات"})


	cypersecurity_list=[]
	host_list=[]
	webservice_list=[]

	for val in cypersecurity:
		data=frappe.get_doc("Package", val["name"])
		cypersecurity_list.append(data)

	for val in host:
		data=frappe.get_doc("Package", val["name"])
		host_list.append(data)

	for val in webservice:
		data=frappe.get_doc("Package", val["name"])
		webservice_list.append(data)


	context.cypersecurity_package=cypersecurity_list
	context.host_package=host_list
	context.webservice_package=webservice_list

	return context