# -*- coding: utf-8 -*-
# Copyright (c) 2015, Nishta and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class BugProject(Document):
	pass

@frappe.whitelist()
def projectwise_data():
	label={"caption":"Project Wise","xAxisName":"Project","yAxisName":"No of Tickets"}
	rdata=[]
	pro_data=frappe.db.sql("Select * from `tabBugProject` where status='active'")
	for pdata in pro_data:
		project_name=pdata[13]
		task_count=frappe.db.count("BugTicket",filters={"project":project_name})
		rdata.append({'label':project_name,'value':task_count})
	result=[{"chart":label,"data":rdata}]
	return result
