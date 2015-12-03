# -*- coding: utf-8 -*-
# Copyright (c) 2015, Nishta and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class BugTicket(Document):
	pass
	def autoname(self):
		bugproj=frappe.get_list("BugProject",fields='*',filters={"project_name":self.project})
		project_count=frappe.db.count("BugTicket",filters={"project":self.project})
		self.ticket_id=bugproj[0]['identifier']+"-0"+str(project_count+1)
		
