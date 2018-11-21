##From the website CodingBat: https://codingbat.com/prob/p153599
##Given a string, this function returns a new string where the first and the
##last characters were exchanged.

def front_back(str):
	n = len(str)
	if n <= 1:
		return(str)
	else:
		return(str[-1]+str[1:n-1]+str[0])
