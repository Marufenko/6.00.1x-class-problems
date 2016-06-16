def item_order(order):
	'''
	The function returns a string that counts the number of each item and consolidates 
	them in the following order: salad:[# salad] hamburger:[# hambruger] water:[# water]
	'''
	import sys
	
	salad_count = 0
	hamburger_count = 0
	water_count = 0
	
	words = order.split()
	
	for word in words:
		if word == 'salad':
			salad_count += 1
		if word == 'hamburger':
			hamburger_count += 1
		if word == 'water':
			water_count += 1
		
	return('salad:' + str(salad_count) + ' hamburger:' + str(hamburger_count) + ' water:' + str(water_count))
