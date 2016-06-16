'''
program prints the number of times the string 'bob' occurs in s
'''

s = 'bobbxbobbofbbobbcosaooboboobobobbobobjj'

sum = 0
x = 0
y = 3

while y <= len(s):
	str = s[x:y]
	if str == 'bob':
		sum += 1
	x += 1
	y+=1
		
print(sum)
