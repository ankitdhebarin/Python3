def find_the_duplicate(l1):

	for i in range(len(l1)):
		for j in range(i+1,len(l1)):

			if l1[i] == l1[j]:
				print("Duplicate number is :", l1[i])
				return l1[i]

print(find_the_duplicate([1,2,1,4,3,12]))
print(find_the_duplicate([6,1,9,5,3,4,9]))