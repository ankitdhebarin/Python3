def sums(nums,target):

	for i in range(len(nums)):
		for j in range(len(nums)):
			if nums[i] + nums[j] == target:
				return (i,j)
			else:
				pass


print(sums([11,2,15,7], 9))
