# -*- coding: utf-8 -*-
# Copyright (c) 2018, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class LoanCollection(Document):
	pass

"""@frappe.whitelist(allow_guest=True)
def update_due_amount(doctype, due_amount = None, customer_loan = None):
	doc_cus_loan = frappe.get_doc("Customer Loan Grant", customer_loan)
	doc_cus_loan.due_amount = due_amount
	doc_cus_loan.save()"""
