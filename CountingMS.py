import random
import time

def splitList(firstList):
	'''
		Function to split list in half
	'''
	midPoint = len(firstList) // 2 #3
	return firstList[:midPoint], firstList[midPoint:] #1

def mergeSortedList(listL, listR, order):
	'''
		Function to take two sorted lists, and merge them in order
	'''
	indexListL = indexListR = 0 #2
	mergedList = [] #1
	targetLength = len(listL) + len(listR) #4

	while len(mergedList) < targetLength: #2n
		if order == 0: #Ascending #n
			if listL[indexListL] <= listR[indexListR]: #2n
				mergedList.append(listL[indexListL]) #n
				indexListL += 1 #2n

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
			mergedList += listL[indexListL:] #1
			break 
		elif indexListL == len(listL): 
			mergedList += listR[indexListR:] 
			break 
	return mergedList #1 

def oneElement(inputList):
	'''
		Function to split list down to a single element, then sort and merge 
	'''
	if len(inputList) <= 1: #3
		return inputList #1
	else:
		listL, listR = splitList(inputList) #3
		return mergeSortedList(oneElement(listL), oneElement(listR), 0) #4 

def MergeSort_Test_Arithmetic_Step(m, n):
	'''
		Function to generate a random array using parameters m and n, keeping m constant
		and calculating n vs runtime
	'''
	arr = []
	for i in range(n):
		arr.append(random.randint(0, m))
	startTime = time.perf_counter()
	oneElement(arr)
	timeElapsed = time.perf_counter() - startTime

	return timeElapsed

def main():
	print(MergeSort_Test_Arithmetic_Step(10**7, 10**6)) #2

if __name__ == "__main__": #1
	main() #1
 
