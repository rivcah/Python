def string_counter(urinput):
	
	count_lower = 0
	count_upper = 0
	count_numbers = 0
	count_other = 0
	
	for l in urinput:
		if l.islower() == True:
			count_lower+=1
		elif l.isupper() == True:
			count_upper+=1
		elif l.isdigit() == True:
			count_numbers+=1
		else:
			count_other+=1
	print("The number of lower case characters is: ", count_lower)
	print("The number of upper case characters is: ", count_upper)
	print("The number of numbers in your string is: ", count_numbers)
	print("All the other things you typed accoun for: ", count_other)
