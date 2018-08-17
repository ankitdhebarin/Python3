def statistics(file):

	with open('Script.txt') as file:
		data = file.readlines()

	return { "lines": len(data),
             "words": sum(len(line.split(" ")) for line in data),
             "characters": sum(len(line) for line in data) }



print(statistics('Script.txt'))