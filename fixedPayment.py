balance = 3929
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12
lowPayment = 0

newBalance = balance
cycles = 0

balance = int(raw_input('enter a new balance: '))
while newBalance > 0:
	lowPayment += 10
	newBalance = balance
	print "Cycle:", cycles
	
	for months in range(0,12):
		newBalance = newBalance + (newBalance * monthlyInterestRate) - lowPayment
		print "Month:", months, "new balance", round(newBalance, 2)
		months += 1
	
	print "Low payment:", lowPayment
	months = 0
	cycles += 1

print "Lowest payment:", round(lowPayment, 2)

