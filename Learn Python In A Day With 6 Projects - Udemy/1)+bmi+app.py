def bmi_app():
	height = input('How tall are you? ')
	weight = input('How much do you weight? ')
	bmi_value = int(weight)/(int(height)/100)**2
	print('Your bmi is {}'.format(round(bmi_value, 2)))
	if bmi_value < 18.5:
	    print('You\'d better eat more!')
	elif bmi_value >= 18.5 and bmi_value <= 24:
	    print('Good job!')
	else:
	    print('You\'d better do some exercises')

bmi_app()
