def sum_pairs(mylist,n):

	size = len(mylist)
	sums = []
	found = False
	for i in range(size):
		for j in range(i+1,size):
			
			if len(sums) != 0:
				return sums

			if mylist[i] + mylist[j] == n:
				sums.append(mylist[i])
				sums.append(mylist[j])
				
	return sums

print(sum_pairs([4,2,10,5,1], 6))
