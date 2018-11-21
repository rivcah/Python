#working with format

def initials(name, surname, year):
    return("Hello {yourname}, your initials are {initials} and your age is {age}.".format(yourname = name+' '+surname, initials = name[0]+surname[0], age = 2018-int(year)))

