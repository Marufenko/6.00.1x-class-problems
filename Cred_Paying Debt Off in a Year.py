'''
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal
'''

balance = 3329
annualInterestRate = 0.2

finished = False;
pay = 0;

def year(pay,myBalance) :
    totalPaid = 0;
    for i in range(1,13):
        totalPaid += pay;
        myBalance = myBalance - pay;
        myBalance = myBalance + ((annualInterestRate/12.0) * myBalance);
        if myBalance<=0 :
            break;
    return myBalance;        
        
while finished == False :
    pay += 10;
    z = year(pay,balance);
    if z <= 0 :
        finished = True;
        print("Lowest Payment: " + str(pay));
