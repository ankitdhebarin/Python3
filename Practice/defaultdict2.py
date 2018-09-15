from collections import defaultdict

def test():

	cities = {'San Francisco': 'US', 'London':'UK',
        'Manchester':'UK', 'Paris':'France',
        'Los Angeles':'US', 'Seoul':'Korea'}

	d1 = defaultdict(list)

	for k,v in cities.items():
		d1[v].append(k)

	return d1

print(test())

