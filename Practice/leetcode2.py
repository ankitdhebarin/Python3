class Node():
	def __init__(self,initdata):
		self.data = initdata
		self.next = None


class Solution():

	def __init__(self):
		self.head = None

	def addTwoNumbers(self,l1,l2):

		#s1 = map(str,l1)
		x1 = ''.join(map(str,l1))
		x2 = ''.join(map(str,l2))
		#s2 = map(str,l2)
		#t1 = ''.join(s1)
		#t2 = ''.join(s2)
		i1 = int(x1)
		i2 = int(x2)

		total = i1 + i2

		return total

s = Solution()
print(s.addTwoNumbers([2,4,3],[5,6,4]))



