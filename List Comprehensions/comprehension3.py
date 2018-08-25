'''
List Comprehension to print first letter of the name and store it in another list
'''
answer = [name[0] for name in ["Elie", "Tim", "Matt"]]
print(answer)

'''
Given 2 lists [1,2,3,4] and [3,4,5,6] create a variable called answer which is a new list that is the intersection of the two. 
Your output should be [3,4].
'''
answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
print(answer)

'''
Given a list of names create variable called answer2 which is a new list with each word reversed and in lower case
'''
answer2 = [name[::-1].lower() for name in ["Elie", "Tim", "Matt"]]
print(answer2)


'''
For all numbers between 1 and 100(including 100) write a list comprehension with all numbers that are divisible by 12
'''
answer = [num for num in range(1,101) if num % 12 == 0]
print(answer)

'''
Given a string "amazing" create a list comprehension containing all the letters from "amazing" but not the vowels('a','e','i','o','u')
'''

answer = [char for char in "amazing" if char not in ('aeiou')]
print(answer)