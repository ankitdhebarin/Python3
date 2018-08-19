def remove_every_other(mylist):

	test = []
	for i,val in enumerate(mylist):
		if i % 2 == 0:
			test.append(val)

	return test

print(remove_every_other([1,2,3,4,5]))
