##From the website CodingBat: https://codingbat.com/prob/p149524
##Given a non-empty string and an intenger, this function removes the character
##number n.


def missing_char(str, n):
    if n <= len(str)-1:
        return(str.replace(str[n], ''))

    
