def isPalindrome(aString):
  '''
  This function takes in a string and returns a boolean.
  if aString is palindrom - True, else - False
  '''

  # delete space
  String=''
  for char in aString:
    if char != ' ':
      String+=char
	
  # compare chars
  length = len(String)
  if length == 0 or length == 1:
	return True
  elif String[0] == String[-1]:
    return isPalindrome(aString[1:-1])
  else:
    return False
