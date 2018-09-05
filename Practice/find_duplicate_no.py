def find_duplicate_no(arr):

	found = False

	for i in range(len(arr)):

		for j in range(i+1,len(arr)):

			if arr[i] == arr[j]:
				found = True
				break

			else:
				pass

	return found

print(find_duplicate_no([1,2,1,4,3,12]))
print(find_duplicate_no([6,1,9,5,3,4,9]))
print(find_duplicate_no([12,3,4,5,6,7]))