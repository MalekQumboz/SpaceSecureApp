import frappe
def get_context(context):


	cypersecurity=frappe.db.sql(""" SELECT * FROM `tabSub Service`where active = 1  and main_services_name = 'خدمة الامن السيبراني' """,as_dict=1)
	host=frappe.db.sql(""" SELECT * FROM `tabSub Service`where active = 1  and main_services_name = 'خدمة الاستضافة' """,as_dict=1)
	webservice=frappe.db.sql(""" SELECT * FROM `tabSub Service`where active = 1  and main_services_name = 'خدمة تصميم المواقع والتطبيقات' """,as_dict=1)

	frappe.db.commit()

	context.cypersecurity_sub=cypersecurity
	context.host_sub=host
	context.webservice_sub=webservice

	return context

