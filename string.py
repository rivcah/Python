##From the website CodingBat
##https://codingbat.com/prob/p189441
##Given a string, this function returns a new string with 'not' added to the
##begging. But if the string already contains 'not', the function returns the
##string, unchanged.

def not_string(str):
	if str[0:3] == 'not':
		return(str)
	elif str[0:3] != 'not':
		return('not '+str)
