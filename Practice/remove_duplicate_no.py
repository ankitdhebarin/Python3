def remove_dups(arr):

	unique = []

	for i in range(len(arr)-1):

		for j in range(i+1,len(arr)-1):

			if arr[i] == arr[j]:

				arr.pop(j)
			

	return arr

print(remove_dups([1,2,3,2,3,5,6,4,6,10]))