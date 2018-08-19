def same_frequency(n1,n2):

	d1 = {}
	d2 = {}
	s1 = str(n1)
	s2 = str(n2)

	count = 1
	for i in range(len(s1)):
		
		if s1[i] in d1:
			d1[s1[i]] += 1

		else:
			d1[s1[i]] = count

	for i in range(len(s2)):
		
		if s2[i] in d2:
			d2[s2[i]] += 1

		else:
			d2[s2[i]] = count

	if d1 == d2:
		return True
	else:
		return False

print(same_frequency(551122,221515))
print(same_frequency(321142,3212215))
