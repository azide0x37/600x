
#annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate / 12
lowPayment = 0
#balance = float(raw_input('enter a new balance: '))
minPay = balance / 12
maxPay = balance * ((1 + monthlyInterestRate)**12 / 12) 
newBalance = balance
found = False

while found == False:
	newBalance = balance
	lowPayment = (minPay + maxPay) / 2
	for months in range(1,13):
		newBalance -= lowPayment
		#print "Month:", months, "New balance:", round(newBalance, 2)
		months += 1		
		newBalance = newBalance + (newBalance * monthlyInterestRate)
	if newBalance > 0:
		minPay = lowPayment
	elif newBalance <= 0 and (newBalance + 0.001 > 0):
		found = True
	else:
		maxPay = lowPayment
print "Lowest payment:", round(lowPayment,2)
