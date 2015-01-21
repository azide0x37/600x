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
	
	for months in range(1,13):
		newBalance -= lowPayment
		print "Month:", months, "New balance:", round(newBalance, 2)
		months += 1
		newBalance = newBalance + (newBalance * monthlyInterestRate)	
	print "Lowest payment:", lowPayment
