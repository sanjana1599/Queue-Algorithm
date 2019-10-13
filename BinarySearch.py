import random
import time 

def binarySearch(arr, start, end, search):
	'''
		Function to take a sorted array and a search element, and search by 
		splitting search range in half and eliminating the half that does not
		contain the search value
	'''
	mid = (start + end) // 2
	while start <= end:
		if search == arr[mid]:
			return mid
		elif search < arr[mid]:
			return (binarySearch(arr, start, mid - 1, search))
		elif search > arr[mid]:
			return (binarySearch(arr, mid + 1, end, search))
	return -1

def binarySearch_Test_1(m, n, t):
	'''
		Function to create random array of size n with values upto m and
		calculate total runtime for t iterations
	'''	
	
	listgen = []
	for i in range(n):
		listgen.append(random.randint(0, m))
	sortedList = listgen.sort() 
	search = random.choice(sortedList)
	start = time.perf_counter()
	for j in range(t):
		print(binarySearch(sortedList, 0, n - 1, search)) 
	stop = time.perf_counter() - start 

	return stop

def binarySearch_Test_UnitRuntime(m, n, t): 
	'''
		Function to calculate unit runtime of each iteration
	'''
	listgen = []
	for i in range(n):
		listgen.append(random.randint(0, m))
	sortedList = listgen.sort() 
	search = random.choice(sortedList) 
	startTime = time.perf_counter()
	for j in range(t):
		print(binarySearch(arr, start, end, search))
	timeElapsed = time.perf_counter() - startTime

	return (timeElapsed / t) * 1000000 

def binarySearch_BAW_Correct(m, n, t):
	'''
		Function to calculate best, average and worst runtimes for 1000 iterations
	'''
	storeList = []
	for i in range(t):
		arr = []
		for j in range(n):
			arr.append(random.randint(0, m))
		arr.sort()
		startTime = time.perf_counter()
		binarySearch(arr, 0, 9999, random.choice(arr))
		timeElapsed = time.perf_counter() - startTime
		#print(timeElapsed)
		storeList.append(timeElapsed)
		worst = max(storeList)
		best = min(storeList)

	return best, worst


def main():
	#print(binarySearch_Test_1(10, 10, 3))
	#print(binarySearch_Test_UnitRuntime(arr, 0, len(arr)-1, search, 3)) 
	print(binarySearch_BAW_Correct(10**5, 10**4, 10**3))

if __name__ == "__main__":
	main()