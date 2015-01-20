__author__ = 'Alexander'
balance = 5000
annualInterestRate = 0.18
monthlyPaymentRate = 0.02

monthCount=1
unpaidBalance = balance
rate = annualInterestRate / 12
currentPayment = 0

while(monthCount < 12):
	currentPayment = (unpaidBalance * monthlyPaymentRate)  
	unpaidBalance -= currentPayment
	unpaidBalance = (unpaidBalance * rate) + unpaidBalance
	print "Month:", monthCount
	print "Minimum monthly payment:", round(currentPayment,2) 
	print "Remaining balance:", round(unpaidBalance,2)
	monthCount += 1
