def validparenthesis(arr):

	if len(arr) % 2 != 0:
		return arr

	opening = set('([{')

	matching = set([('(',')'),('[',']'),('{','}')])

	stack = []

	for paren in arr:

		if paren in opening:

			stack.append(paren)

		else:

			if len(stack) == 0:
				return False

			last_item = stack.pop()

			if (last_item,paren) not in matching:
				return False

	return len(stack) == 0

print(validparenthesis("()"))
print(validparenthesis("()[]{}"))
print(validparenthesis("(]"))
print(validparenthesis("([)]"))
print(validparenthesis("{[]}"))
