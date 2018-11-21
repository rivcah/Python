##This function displays a monthly calendar

from calendar import *
def cal():
	month_year = {
                'January' : '1',
                'February' : '2',
                'March' : '3',
                'April' : '4',
                'May' : '5',
                'June' : '6',
                'July' : '7',
                'August' : '8',
                'September' : '9',
                'October' : '10',
                'November' : '11',
                'December' : '12'}


	y = int(input("Choose a year: \n"))
	m = input("Choose a month: \n")
	decision = m.isnumeric()
	if decision is False:
		m = int(month_year[m])
	cal = month(y, m)
	print("\n \n This is your calendar:\n")
	print(cal)
