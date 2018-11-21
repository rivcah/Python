##Given an intenger n, the function returns the absolute difference between n and
##21. It returns the double of the absolute difference if n is greater than 21.
##From the website CodingBat
##https://codingbat.com/prob/p197466

def diff21(n):
	if n <= 21:
		return(abs(21-n))
	elif n > 21:
		return(2*abs(21-n))
