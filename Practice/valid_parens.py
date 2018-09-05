def valid_parens(st):

	opening = set('([{')

	matching = set([('(',')'), ('{','}'), ('[', ']')])

	stack = []

	if len(st) % 2 != 0:
		return False

	else:

		for paren in st:

			if paren in opening:

				stack.append(paren)

			else:

				last_item = stack.pop()

				if (last_item,paren) not in matching:

					return False


	return len(stack) == 0

st = "[()]"
print(valid_parens(st))
