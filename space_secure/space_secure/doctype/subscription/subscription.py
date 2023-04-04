# Copyright (c) 2023, MalekQumboz and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Subscription(Document):
	def before_validate(self):
		self.get_total_subscription_days()
		self.get_total_price()

	def get_total_subscription_days(self):
		total_subscription_days = 0
		if self.start_date and self.end_date:
			total_subscription_days = frappe.utils.date_diff(self.end_date, self.start_date) + 1
		if total_subscription_days >= 0:
			self.total_subscription_days =total_subscription_days
		else:
			return 0

	def get_total_price(self):
		package_price = frappe.db.sql(""" SELECT price FROM `tabPackage`where package_name = %s """,
									  (self.package_name), as_dict=1)
		if self.total_subscription_days:
			self.total_price=(package_price[0].price/30) * self.total_subscription_days
		else:
			self.total_price =0



@frappe.whitelist()
def get_total_subscription_days(start_date=None ,end_date=None):
	total_subscription_days = 0
	if start_date and end_date:
		total_subscription_days = frappe.utils.date_diff(end_date, start_date) + 1
	if total_subscription_days >= 0:
		return total_subscription_days
	else:
		return 0