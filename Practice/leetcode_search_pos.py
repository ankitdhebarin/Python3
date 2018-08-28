def search_insertpos(arr,num):

	for i,j in enumerate(range(len(arr))):

		if arr[j] == num:
			return i

		pass

print(search_insertpos([1,3,5,6],5))



