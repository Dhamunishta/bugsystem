# -*- coding: utf-8 -*-
# Copyright (c) 2015, Nishta and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

@frappe.whitelist()
def bug_request():
	label={"caption": "Project wise Bug and Request",
        "showlabels": "1",
        "showvalues": "1",
        "decimals": "0",
        "placevaluesinside": "1",
        "rotatevalues": "1",
        "bgcolor": "FFFFFF",
        "legendshadow": "0",
        "legendborderalpha": "50",
        "canvasborderthickness": "1",
        "canvasborderalpha": "50",
        "showBorder": "0"}
	bugdata=[]
	reqdata=[]
	category=[]
	pro_data=frappe.db.sql("Select * from `tabBugProject` where status='active'")
	for pdata in pro_data:
		project_name=pdata[13]
		category.append({'label':project_name})
		bug_count=frappe.db.count("BugTicket",filters={"project":project_name,"features":"Bug"})
		req_count=frappe.db.count("BugTicket",filters={"project":project_name,"features":"Request"})
		bugdata.append({'value':bug_count})
		reqdata.append({'value':req_count})
	dataset=[{'seriesname':'Bug','data':bugdata},{'seriesname':'Request','data':reqdata}]
	categories=[{'category':category}]
	#dataset=['dataset']
	result=[{"chart":label,"categories":categories,"dataset":dataset}]
	return result
