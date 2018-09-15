from collections import defaultdict

def count():

	d1 = defaultdict(list)

	L = [1,2,4,8,16,32,64,128,256,512,1024,32768,65536,4294967296]

	for i in L:

		d1[len(str(i))].append(i)

	return d1

print(count())


