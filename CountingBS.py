import random
import time

def binarySearch(arr, start, end, search):
	mid = (start + end) // 2 #3
	while start <= end: #2(log n to the base 2)
		if search == arr[mid]: #1(log n to the base 2)
			return mid #1
		elif search < arr[mid]: #1(log n to the base 2)
			return (binarySearch(arr, start, mid - 1, search)) #2(log n to the base 2)
		else:
			return (binarySearch(arr, mid + 1, end, search)) #2
	return -1 #1

def binarySearch_Test_Arithmetic_Step(m, n): 
	'''
	Function to take input 'n' size of array, max value 'm' is one power more than n, keep 
	m constant and calculate n vs runtime
	'''
	arr = []
	for j in range(n):
		arr.append(random.randint(0, m))
	arr.sort()
	startTime = time.perf_counter()
	binarySearch(arr, 0, len(arr)-1, random.choice(arr))
	timeElapsed = time.perf_counter() - startTime
	print(timeElapsed)

	return -1

def main():
	#print(binarySearch([2, 18, 27, 40, 72, 93, 101], 0, 6, 2)) #2
	print(binarySearch_Test_Arithmetic_Step(10**7, 10**6))

if __name__ == "__main__": #1
	main() #1





