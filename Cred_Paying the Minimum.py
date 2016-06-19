'''
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal
'''

balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

month = 0
total_paid = 0
rem_bal = balance

while month < 12:
	month += 1
	min_mon_pay = rem_bal * monthlyPaymentRate
	rem_bal = (rem_bal - min_mon_pay) + ((annualInterestRate/12.0)*(rem_bal - min_mon_pay))
	print("Month: " + str(month))
	print("Minimum monthly payment: " + str(round(min_mon_pay, 2)))
	print("Remaining balance: " + str(round(rem_bal, 2)))
	
	total_paid += min_mon_pay

print("Total paid: " + str(round(total_paid, 2)))
print("Remaining balance: " + str(round(rem_bal, 2)))
