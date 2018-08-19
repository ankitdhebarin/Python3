def remove_every_other(mylist):

	size = len(mylist)

	for i in range(size):
		if i % 2 == 1:
			mylist.pop(i)

	print(mylist)

remove_every_other([1,2,3,4,5])
