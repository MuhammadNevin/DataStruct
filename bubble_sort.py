# Python program for implementation of Bubble Sort

from pyrsistent import s


def bubbleSort(arr):
	n = len(arr)
	# optimize code, so if the array is already sorted, it doesn't need
	# to go through the entire process
	# Traverse through all array elements
	# for i in list:
    #  	s
    
	# n = 7
	for i in range(n-1):
        # flag check is it sorted?
		swapped = False 
    	# range(n) also work but outer loop will
		# repeat one time more than needed.
		# Last i elements are already in place
		print("iterasi ke :", i)
		print(arr)
		for j in range(0, n-i-1): #range(0, n-i-1) = range(0, 7-0-1) = range(6) = [0, 1, 2, 3, 4, 5]
			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
		#    int() -> convert ke integer
			print(arr[j], ":" ,arr[j + 1])
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
		# print("iterasi :", str(i), arr)
		
		if not swapped:
			# if we haven't needed to make a single swap, we
			# can just exit the main loop.
			return


# Driver code to test above
# arr = [7, 1, 3, 5, 6]
arr = [99, 7, 3, 2, 6]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
	print("% d" % arr[i], end=" ")
