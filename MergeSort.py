import random
import time

def splitList(firstList):
	'''
		Function to split list in half
	'''
	midPoint = len(firstList) // 2
	return firstList[:midPoint], firstList[midPoint:] 

def mergeSortedList(listL, listR, order):
	'''
		Function to take two sorted lists, and merge them in order
	'''
	indexListL = indexListR = 0
	mergedList = []
	targetLength = len(listL) + len(listR) 

	while len(mergedList) < targetLength:
		if order == 0: #Ascending
			if listL[indexListL] <= listR[indexListR]:
				mergedList.append(listL[indexListL])
				indexListL += 1

			else:
				mergedList.append(listR[indexListR])
				indexListR += 1
		else: #Descending
			if listL[indexListL] >= listR[indexListR]:
				mergedList.append(listL[indexListL])
				indexListL += 1

			else:
				mergedList.append(listR[indexListR])
				indexListR += 1

		if indexListR == len(listR):
			mergedList += listL[indexListL:]
			break
		elif indexListL == len(listL):
			mergedList += listR[indexListR:]
			break
	return mergedList 

def oneElement(inputList):
	'''
		Function to split list down to a single element, then sort and merge 
	'''
	if len(inputList) <= 1:
		return inputList
	else:
		listL, listR = splitList(inputList)
		return mergeSortedList(oneElement(listL), oneElement(listR), 0) #ascending order

def mergeSort_Test_1(m, n, t):
	'''
		Function to generate a random list of size n, containing elements of value
		lesser than m, and calculate total runtime for t iterations
	'''
	lis = []
	for i in range(n):
		lis.append(random.randint(0, m)) 
	start = time.perf_counter()
	for i in range(t):
		oneElement(lis)
	stop = time.perf_counter() - start 

	return stop

def mergeSort_Test_2(m, n, t):
	'''
		Function same as above, except calculating unit runtime instead of total
		runtime
	'''
	lis = []
	for i in range(n):
		lis.append(random.randint(0, m)) 
	start = time.perf_counter()
	for i in range(t):
		oneElement(lis)
	stop = time.perf_counter() - start 

	return (stop / t) 

def mergeSort_BAW_Correct(m, n, t):
	'''
		Function to calculate best, average and worst runtimes for 1000 iterations
	'''
	storeList = []
	for i in range(t):
		lis = []
		for j in range(n):
			lis.append(random.randint(0, m))
		startTime = time.perf_counter()
		oneElement(lis)
		timeElapsed = time.perf_counter() - startTime
		#print(timeElapsed)
		storeList.append(timeElapsed)
		worst = max(storeList)
		best = min(storeList)

	return best, worst

def main():
	#print(oneElement([23, 788, 176, 223, 9000, 2, 1, 0, 42])) 
	#print(mergeSort_Test_1(10**6, 10**3, 10**2)) 
	#print(mergeSort_Test_2(10**2, 50, 10)) 
	print(mergeSort_BAW_Correct(10**5, 10**4, 10**3))

if __name__ == "__main__":
	main()