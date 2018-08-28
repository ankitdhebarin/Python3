def merge_lists(l1,l2):

	res = []

	while l1 and l2:

		if l1[0] < l2[0]:

			res.append(l1.pop(0))

		else:
			res.append(l2.pop(0))

	return res

print(merge_lists([1,2,5,8,0], [1,3,7]))