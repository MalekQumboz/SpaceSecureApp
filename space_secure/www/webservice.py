import frappe
def get_context(context):

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

	frappe.db.commit()


	context.cypersecurity_sub=cypersecurity_list
	context.host_sub=host_list
	context.webservice_sub=webservice_list

	return context

