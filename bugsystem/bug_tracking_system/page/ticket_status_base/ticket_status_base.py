# -*- coding: utf-8 -*-
# Copyright (c) 2015, Nishta and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

@frappe.whitelist()
def ticket_status_data():
	label={"caption": "Ticket Status","subCaption": "Base Report","startingAngle": "120","showLabels": "0","showLegend": "1","enableMultiSlicing": "0","slicingDistance": "15","showPercentValues": "1","showPercentInTooltip": "0","theme": "fint"}
	rdata=[]
	ticket_status_data=frappe.db.sql("Select status from `tabBugTicket Status`")
	for sdata in ticket_status_data:
		status=sdata[0]
		task_count=frappe.db.count("BugTicket",filters={"status":status})
		rdata.append({'label':status,'value':task_count})
	result=[{"chart":label,"data":rdata}]
	return result