def valid_parenthesis(s):

	if len(s) % 2 != 0:
		return False

	stack = []

	opening = set('([{')

	matching = set([('(',')'), ('{','}'), ('[',']')])

	for paren in s:

		if paren in opening:

			stack.append(paren)

		else:

			if len(s) == 0:
				return False

			last_item = stack.pop()

			if (last_item,paren) not in matching:
				return False

	return len(stack) == 0


print(valid_parenthesis('{[]}'))


