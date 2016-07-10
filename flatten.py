def flatten(aList):
'''
Write a function to flatten a list. The list contains other lists, strings, or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5]
'''
  i=0
  while i<len(aList):
    while True:
      try:
        aList[i:i+1] = aList[i]
      except (TypeError, IndexError):
        break
    i += 1
  return aList
