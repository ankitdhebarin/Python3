def mergeTwoLists(l1, l2):

	res = []

	#print(max(l1,l2))

	while l1 and l2:

		if l1[0] == l2[0]:
			res.append(l1.pop(0))
		else:
			res.append(l2.pop(0))


	return sorted(res + l1 + l2)

print(mergeTwoLists([1,2], [1,3,7]))

