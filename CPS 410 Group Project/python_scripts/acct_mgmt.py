#!/usr/bin/python

from emp_mgmt import *
import sys
import sqlite3

account_list = []

class Account(object):

	def __init__(self, cust_name, phone_number, cust_id, init_date, est_date, book_date, price):
		self.cust_name = cust_name
		self.phone_number = phone_number
		self.cust_id = cust_id
		self.init_date = init_date
		self.est_date = est_date
		self.book_date = book_date
		self.est_price = price

	def get_cust_name(self):
		return self.cust_name

	def get_cust_id(self):
		return self.cust_id

	def get_init_date(self):
		return self.init_date

	def get_phone_number(self):
		return self.phone_number

	def set_est_date(self, setting_est_date):
		self.est_date = self.setting_est_date

	def get_est_date(self):
		return self.est_date

	def set_book_date(self, setting_book_date):
		self.book_date = self.setting_book_date

	def get_book_date(self):
		return self.book_date

	def set_est_price(self, setting_est_price):
		self.est_price = self.setting_est_price

	def get_est_price(self):
		return self.est_price

	def add_account(self):
		account_list.append(self)

	def to_string(self):
		print "Customer Name: " + self.get_cust_name() + ", Cust. ID: " + (str)(self.get_cust_id())
		print "Phone: " + self.get_phone_number()
		print "Initial Date of Contact: " + self.get_init_date()
		print "Date of Estimate: " + self.get_est_date()
		print "Date of Job Booking: " + self.get_book_date()
		print "Estimated Price of job: " + (str)(self.get_est_price())

a1 = Account("Mi gao", "867-5309", 0, "12/30/15", "2/25/16", "5/1/16", 0)
a1.add_account()

a2 = Account("Teresa Robinson", "863-6043", 1, "12/31/15", "2/20/16", "5/3/16", 0)
a2.add_account()

print "Modification? (Choose a letter non-case sensitive)"
print "A) Add an account"
print "B) View an account"
print "C) Remove or Edit an account"
print "D) Close out an account"

choice = raw_input()
conn = sqlite3.connect('test.db')
# add an account
if choice is "A" or choice is "a":
	print "Name: "
	name = raw_input()
	
	# change to reference the last previously used CID + 1
	cid = (int)(a2.get_cust_id()) + 1

	print "Phone: "
	phone = raw_input()	

	print "Init. date of contact: "
	init_date = raw_input()

	print "Est. date (if known, else n/a): "
	est_date = raw_input()
	print "Booking date (if known, else n/a): "
	booking_date = raw_input()
	print "Price (if known, else n/a): "
	est_price = raw_input()

	a = Account(name, phone, cid, init_date, est_date, booking_date, est_price)
	a.to_string()

# view an account or all accounts
elif choice is "B" or choice is "b":
	print "Which account would you like to view? (Choose a number)"
	for i in range(0, len(account_list)):
		print str(i) + " " + str(account_list[i].get_cust_name())
	view_acct = raw_input()
	

# remove or edit an account
elif choice is "C" or choice is "c":
	looper = True
	while looper is True:

		# print C menu
		print "Would you like to edit an account, or remove it?"
		print "0: Edit"
		print "1: Remove"
		print "C: Cancel"

		c_choice = raw_input()
		if c_choice is "0":

			# print account list
			print "Which account would you like to edit? (Choose a number)"
			for i in range(0, len(account_list)):
				print str(i) + " " + str(account_list[i].get_cust_name())

			# print specified account information
			c0_choice = raw_input()
			print account_list[(int)(c0_choice)].to_string()
			looper = False
			# what field would you like to edit?
			# enter a new value for field
			# set value

		elif c_choice is "1":
			print "Which account would you like to remove? (Choose a number)"
			for i in range(0, len(account_list)):
				print str(i) + " " + str(account_list[i].get_cust_name())

			print "Are you sure about this?  Type Y to confirm:"
			c1_choice = raw_input()
			
			if c1_choice is "y" or c1_choice is "Y":
				print "Accounts are removed in this logic spot"
				looper = False
			else:
				print "No accounts have been removed."
		
		elif c_choice is "C" or c_choice is "c":
			print "Cancelled"
			sys.exit(0)
		
		else:
			print "Invalid menu input. Please try again."


# close out accounts
elif choice is "D" or choice is "d":
	print "You chose D"
	print "Which account would you like to close out? (Choose a number)"
	for i in range(0, len(account_list)):
		print str(i) + " " + str(account_list[i].get_cust_name())
	c0_choice = raw_input()
	# we are not actually removing an account yet
	print "removed " + account_list[(int)(c0_choice)].to_string()
	looper = False

	# take the account, remove it from the active account list,
	# designate in the file write that the account was closed in the period 

# else not abcd
else:
	print "Invalid input. Please try again."
conn.close()

if __name__ == '__main__':
	sys.exit(0)
