def range_in_list(l1,start,end):

	count = 0

	for i in range(start,end+1):

		count = count + l1[i]

	return count


print(range_in_list([1,2,3,4],0,2))
print(range_in_list([1,2,3,4],0,3))