##Given two integer values, this function returns their sum.
##If the two values are the same, it returns the double of their sum.
##From the website CodingBat (codingbat.com)
##https://codingbat.com/prob/p141905

def sum_double(a, b):

    if a != b:
        return(a+b)
    elif a == b:
        return(2*(a+b))


    
