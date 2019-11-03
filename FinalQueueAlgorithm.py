import random

def itemCalculate(extraPaymentTime):
	scanTime = [7, 3, 2, 3, 16, 11, 3, 5, 6, 3, 17, 10, 4, 4, 3, 3, 6] #real readings 
	extraScanTime = 0
	bagTime = 3
	listOfCategories = ["Clothing", "Food"]
	answer = ["Yes", "No"]
	noOfItems = random.randint(1, 20)
	for i in range(noOfItems):
		itemCategory = random.choice(listOfCategories) 
		itemDiscount = random.choice(answer) 
		if itemCategory == "Clothing": 
			extraScanTime += 10
		if itemDiscount == "Yes": 
			extraScanTime += 10
	serviceTime = (noOfItems * (random.choice(scanTime) + bagTime)) + extraScanTime + extraPaymentTime   

	return serviceTime

def firstCustomerCalc(temp_serviceTime):	
	serviceTime1 = 0
	minusPaymentTime = 0
	first = random.randint(1,4)
	if first == 1:
		minusPaymentTime = 0.25 #just started
	elif first == 2:
		minusPaymentTime = 0.5 #halfway through
	else:
		minusPaymentTime = 0.75 #almost done
	serviceTime1 = temp_serviceTime - (minusPaymentTime * temp_serviceTime)

	return serviceTime1

def customerCalculate():
	extraPaymentTime = 0
	paymentMethod = ["Cash", "Card"]
	cashPayment = [55, 46, 37, 29, 30, 13, 9, 18, 51, 19, 83, 17, 18, 22, 34] #real readings
	cardPayment = [64, 52, 29, 34, 46, 55, 57, 61, 43, 33, 30, 37, 52, 49, 43] #real readings
	customerPaymentMethod = random.choice(paymentMethod)
	answerM = ["Yes", "No, but I want membership", "No, I don't want membership"]
	customerMembership = random.choice(answerM)
	if customerPaymentMethod == "Cash":
		extraPaymentTime += random.choice(cashPayment)
	else:
		extraPaymentTime += random.choice(cardPayment)
	if customerMembership == "Yes":
		extraPaymentTime += 15
	elif customerMembership == "No, but I want membership":
		extraPaymentTime += 25 

	return 	itemCalculate(extraPaymentTime) 

def SecondsToMinutes(inp):
	ans = inp // 60
	rem = inp % 60
	queueTime = str(ans) + " minutes " + str(rem) + " seconds "

	return queueTime 

def TestCase_1_noOfCustomers():
	queueTime = []
	lis = [3, 5, 6, 7]
	for i in lis: 
		serviceTime = 0
		for j in range(i): 
			serviceTime += customerCalculate()
		queueTime.append(SecondsToMinutes(serviceTime))

	return queueTime 

def itemCalculate_Test(extraPaymentTime, noOfItems):
	scanTime = [7, 3, 2, 3, 16, 11, 3, 5, 6, 3, 17, 10, 4, 4, 3, 3, 6] #real readings 
	extraScanTime = 0
	bagTime = 3
	listOfCategories = ["Clothing", "Food"]
	answer = ["Yes", "No"] 
	for i in range(noOfItems):
		itemCategory = random.choice(listOfCategories) 
		itemDiscount = random.choice(answer) 
		if itemCategory == "Clothing": 
			extraScanTime += 10 
		if itemDiscount == "Yes": 
			extraScanTime += 10 
	serviceTime = (noOfItems * (random.choice(scanTime) + bagTime)) + extraScanTime + extraPaymentTime   

	return serviceTime

def TestCase_2_totalItems():
	queueTime = []
	lis = [67, 175, 197, 210]
	for i in lis:
		queueTime.append(SecondsToMinutes(itemCalculate_Test(20, i))) #20 sec assigned as avg extra paytime

	return queueTime


def main():
	#print(TestCase_1_noOfCustomers()) #analysis (a)
	#print(TestCase_2_totalItems()) #analysis (b)
	queueTimeList = []
	queueTimeList_minSec = []
	noOfQueues = random.randint(2, 6) 
	#print("Queues ", noOfQueues)
	for i in range(noOfQueues):
		serviceTimeList = [] 
		noOfCustomers = random.randint(1, 7) 
		firstCustomer = True
		#print("Customers ", noOfCustomers)
		for j in range(noOfCustomers):
			if firstCustomer == True:
				temp_serviceTime = customerCalculate()
				serviceTimeList.append(firstCustomerCalc(temp_serviceTime)) 
				firstCustomer = False
			else:
				serviceTimeList.append(customerCalculate()) 
		queueTimeList.append(sum(serviceTimeList)) 
		queueTimeList_minSec.append(SecondsToMinutes(sum(serviceTimeList))) 
	print(queueTimeList_minSec)

if __name__ == "__main__":
	main()
