annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12
lowPayment = 0
newBalance = balance
months = 0
cycles = 0

while newBalance > 0:
	newBalance = balance
	lowPayment += 10
	#print "Cycle:", cycles
	
	while months < 12:
		newBalance = newBalance + (newBalance * monthlyInterestRate) - lowPayment
		#print "Month:", months, "new balance", round(newBalance, 2)
		months += 1
	
	#print "Low payment:", lowPayment
	
	months = 0
	cycles += 1

print "Lowest payment", round(lowPayment, 2)

