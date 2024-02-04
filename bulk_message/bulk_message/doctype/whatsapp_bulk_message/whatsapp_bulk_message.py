# Copyright (c) 2023, tejal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
class WhatsappBulkMessage(Document):
		
	def before_save(self):
		self.to_send_massage()

	@frappe.whitelist()
	def get_user_registration_data(self):
		if self.get('whatsapp_template'):
			doc = frappe.get_all("User Registration", 
							filters={'wtsp_number': ('is', 'set')},
							fields=["user_name","wtsp_number"],
							group_by="wtsp_number")
			
			if(doc):
				for d in doc:
					self.append('user_registration_child_table_data', {
												"user_name":d.user_name,
												"whatsapp_number":d.wtsp_number})
	@frappe.whitelist()
	def to_send_massage(self):				
		for d in self.get('user_registration_child_table_data'):
			if d.whatsapp_number:
				doc1=frappe.new_doc("Whatsapp Bulk Log")
				doc1.whatsapp_number=d.whatsapp_number
				doc1.user_name=d.user_name
				doc1.save()


	@frappe.whitelist()
	def set_template(self):				
		for d in self.get('user_registration_child_table_data'):
			if d.whatsapp_number:
				doc1=frappe.new_doc("Whatsapp Bulk Log")
				doc1.whatsapp_number=d.whatsapp_number
				doc1.user_name=d.user_name
				doc1.save()


	@frappe.whitelist()
	def selected_(self):
		if self.get('whatsapp_template'):
			notification_entry = frappe.get_doc("WhatsApp Notification", {"name": "WN-0028"})
			notification_entry.template = self.whatsapp_template
			notification_entry.save()

