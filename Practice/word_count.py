def count_words(filename):

	d = {}

	with open(filename) as file:

		for word in file.read().split():

			if word not in d:
				d[word] = 1

			else:
				d[word] += 1

	return d

print(count_words("data.txt"))