def max_dictionary_value(l1):

	dict1 = {}

	for i in range(len(l1)-1):

		if l1[i] in dict1:

			dict1[l1[i]] += 1

		else:

			dict1[l1[i]] = 1

	sorted_dict = sorted(dict1.items(),key = lambda kv: kv[1])

	print(sorted_dict)

max_dictionary_value([4,4,4,4,3,3,2,2,2,2,2,1,1,1])



