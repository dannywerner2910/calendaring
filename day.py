e = 'Your input is invalid, Please try again!'
def val_or_not(d, m, y):
	if type(d) != int or type(m) != int or type(y) != int:
		return 'Invalid'
	else:
		if y > 1:
			return 'Valid'
		elif y < 1:
			return 'Invalid'
		else:
			if m > 1:
				return 'Valid'
			elif m < 1:
				return 'Invalid'
			else:
				if d >= 1:
					return 'Valid'
				else:
					return 'Invalid'

def count(d, m, y):
	dd = d - 1
	dm = (m-1)*30
	dy = (y-1)*365
	for i in range(1, y):
		if i%100 == 0 and i%400 != 0:
			dy = dy - 1
	while m > 1:
		if m in [2, 4, 6, 8, 9, 11]:
			dm = dm + 1
		elif m == 3:
			dm = dm - 2
		m = m - 1
	if y%4 == 0 and m > 2:
		if y%100 == 0 and y%400 != 0:
			pass
		else:
			dy = dy + 1
		y = y - 1
	while y > 1:
		if y%4 == 0:
			dy = dy + 1
		y = y - 1
	res = dd + dm + dy
	return res

print('Note: you can only check the day of a date since the year 1 A.D.')
print('Please input the dates here:')
while True:	
	d = int(input('Date: '))
	m = int(input('Month: '))
	y = int(input('Year: '))
	if val_or_not(d, m, y) == 'Invalid':
		print(e)
		continue
	else:
		a = count(d, m, y)
		i = a%7
		if i == 5:
			print ('%d/%d/%d is Saturday'%(d, m, y))
		elif i == 6:
			print('%d/%d/%d is Sunday'%(d, m, y))
		elif i == 0:
			print('%d/%d/%d is Monday'%(d, m, y))
		elif i == 1:
			print('%d/%d/%d is Tuesday'%(d, m, y))
		elif i == 2:
			print('%d/%d/%d is Wednesday'%(d, m, y))
		elif i == 3:
			print('%d/%d/%d is Thursday'%(d, m, y))
		else:
			print('%d/%d/%d is Friday'%(d, m, y))
		break
