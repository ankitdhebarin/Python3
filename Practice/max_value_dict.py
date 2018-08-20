def max_value(arr):

	count = 1
	dict = {}

	newlist = set(arr)

	for i in arr:

		if i in dict:			
			dict[i] += 1
		else:
			dict[i] = count

	#sorted_by_value = sorted(dict.values())[-1]
	#sorted_by_value = sorted(dict.items(), key=lambda kv: kv[1])	
	sorted_by_value = sorted(dict.items(), key = lambda kv: kv[1])
	
	return (sorted_by_value).pop()

print(max_value([4,4,4,4,3,3,2,2,2,2,2,1,1,1]))

