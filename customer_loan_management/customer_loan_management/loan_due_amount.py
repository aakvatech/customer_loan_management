from __future__ import unicode_literals
import frappe
from frappe import msgprint
from frappe.model.document import Document
from frappe.utils import flt

@frappe.whitelist(allow_guest=True)
def update_due_amount(doctype, due_amount = None, customer_loan = None):
	doc_cus_loan = frappe.get_doc("Customer Loan Grant", customer_loan)
	doc_cus_loan.due_amount = due_amount
	doc_cus_loan.save()

@frappe.whitelist(allow_guest=True)
def update_outstanding_amount(doctype, total_outstanding_amount = None, customer_loan = None):
	doc_cus_loan = frappe.get_doc("Customer Loan Grant", customer_loan)
	doc_cus_loan.total_outstanding_amount = total_outstanding_amount
	doc_cus_loan.save()


@frappe.whitelist(allow_guest=True)
def update_rece_account(doctype, date = None, accounts_receivable = None, loan_amount = None, customer = None, name = None):
	gl_entry = frappe.get_doc({
	"doctype": "GL Entry", 
	"posting_date": date,
	"party": customer,
	"voucher_type":"Customer Loan Grant",
	"party_type":"Customer",
	"voucher_no":name,
	"account":accounts_receivable,
	"debit":loan_amount,
	"debit_in_account_currency":loan_amount
	})
	gl_entry.insert(ignore_permissions=True)
	gl_entry.submit()


@frappe.whitelist(allow_guest=True)
def update_cash_account(doctype, cash_account = None, date = None, loan_amount = None, customer = None, name = None):
	gl_entry = frappe.get_doc({
	"doctype": "GL Entry", 
	"posting_date": date,
	"party": customer, 
	"voucher_type":"Customer Loan Grant",
	"party_type":"Customer",
	"voucher_no":name,
	"account":cash_account,
	"credit":loan_amount,
	"credit_in_account_currency":loan_amount
	})
	gl_entry.insert(ignore_permissions=True)
	gl_entry.submit()


########################		Installment Account Code                ############################################################


@frappe.whitelist(allow_guest=True)
def update_instalment_amount_ca(doctype, cash_account = None, date = None, instalment_amount = None, customer = None, name = None):
	gl_entry = frappe.get_doc({
	"doctype": "GL Entry", 
	"posting_date": date,
	"party": customer, 
	"voucher_type":"Loan Collection",
	"party_type":"Customer",
	"voucher_no":name,
	"account":cash_account,
	"debit":instalment_amount,
	"debit_in_account_currency":instalment_amount
	})
	gl_entry.insert(ignore_permissions=True)
	gl_entry.submit()


@frappe.whitelist(allow_guest=True)
def update_instalment_amount_ar(doctype, accounts_receivable = None, date = None, instalment_amount = None, customer = None, name = None):
	gl_entry = frappe.get_doc({
	"doctype": "GL Entry", 
	"posting_date": date,
	"party": customer, 
	"voucher_type":"Loan Collection",
	"party_type":"Customer",
	"voucher_no":name,
	"account":accounts_receivable,
	"credit":instalment_amount,
	"credit_in_account_currency":instalment_amount
	})
	gl_entry.insert(ignore_permissions=True)
	gl_entry.submit()


############################		Penalty Account Code                ###############################################################


@frappe.whitelist(allow_guest=True)
def update_penalty_amount(doctype, penalty_income_account = None, date = None, penalty_amount = None, customer = None, name = None):
	gl_entry = frappe.get_doc({
	"doctype": "GL Entry", 
	"posting_date": date,
	"party": customer, 
	"voucher_type":"Loan Collection",
	"party_type":"Customer",
	"voucher_no":name,
	"account":penalty_income_account,
	"credit":penalty_amount,
	"credit_in_account_currency":penalty_amount
	})
	gl_entry.insert(ignore_permissions=True)
	gl_entry.submit()

@frappe.whitelist(allow_guest=True)
def update_penalty_amount_ar(doctype, accounts_receivable = None, date = None, penalty_amount = None, customer = None, name = None):
	gl_entry = frappe.get_doc({
	"doctype": "GL Entry", 
	"posting_date": date,
	"party": customer, 
	"voucher_type":"Loan Collection",
	"party_type":"Customer",
	"voucher_no":name,
	"account":accounts_receivable,
	"debit":penalty_amount,
	"debit_in_account_currency":penalty_amount
	})
	gl_entry.insert(ignore_permissions=True)
	gl_entry.submit()


############################		Interest Account Code                ###############################################################


@frappe.whitelist(allow_guest=True)
def update_interest_amount(doctype, interest_income_account = None, date = None, interest_amount = None, customer = None, name = None):
	gl_entry = frappe.get_doc({
	"doctype": "GL Entry", 
	"posting_date": date,
	"party": customer, 
	"voucher_type":"Customer Loan Grant",
	"party_type":"Customer",
	"voucher_no":name,
	"account":interest_income_account,
	"credit":interest_amount,
	"credit_in_account_currency":interest_amount
	})
	gl_entry.insert(ignore_permissions=True)
	gl_entry.submit()

@frappe.whitelist(allow_guest=True)
def update_interest_amount_ar(doctype, accounts_receivable = None, date = None, interest_amount = None, customer = None, name = None):
	gl_entry = frappe.get_doc({
	"doctype": "GL Entry", 
	"posting_date": date,
	"party": customer, 
	"voucher_type":"Customer Loan Grant",
	"party_type":"Customer",
	"voucher_no":name,
	"account":accounts_receivable,
	"debit":interest_amount,
	"debit_in_account_currency":interest_amount
	})
	gl_entry.insert(ignore_permissions=True)
	gl_entry.submit()
