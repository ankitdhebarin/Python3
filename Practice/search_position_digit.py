def search_position_digit(arr,num):

	found = False

	for i in range(len(arr)-1):

		if arr[i] == num:

			found = True
			return i

		else:
			pass

	if found == False:
		print("Couldnt find the number in the list")


print(search_position_digit([1,2,3,4,5],3))

