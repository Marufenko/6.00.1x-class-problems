'''
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s.
'''

s='ddddaoophphphph'

sum = 0
for char in s:
	if char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
		sum += 1
print(sum)
