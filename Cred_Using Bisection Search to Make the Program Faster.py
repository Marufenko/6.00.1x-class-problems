'''
Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year. Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). Produce the same return value as you did in Problem 2.
'''

balance = 3329
annualInterestRate = 0.2

lower = balance/12.0
upper = balance*((1+annualInterestRate/12.0)**12)

finished = False
pay = (lower + upper)/2

def year(pay,myBalance) :
    totalPaid = 0
    for i in range(1,13):
        totalPaid += pay
        myBalance = myBalance - pay
        myBalance = myBalance + ((annualInterestRate/12.0) * myBalance)
        if myBalance <= 0:
            break
    return myBalance
		
while True:
    z = year(pay,balance)
    if abs(z-0.01)<0.1:
       print("Lowest Payment: " + str(pay))
       break   
    elif z<0:
       upper = pay
       pay = round((upper+lower)/2,2)
    else :
       lower = pay
       pay = round((upper+lower)/2,2)
