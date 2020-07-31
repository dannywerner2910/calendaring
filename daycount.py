class Counter:
	def __init__(self, d, m, y, d1, m1, y1):
		self.d = d
		self.m = m
		self.y = y
		self.d1 = d1
		self.m1 = m1
		self.y1 = y1
	def count(self):
		dd = self.d1 - self.d
		dm = (self.m1 - self.m)*30
		dy = (self.y1 - self.y)*365
		for i in range(self.y, self.y1):
			if i%100 == 0 and i%400 != 0:
				dy = dy - 1
		if self.y%4 == 0 and self.m <= 2:
			if self.y%100 == 0 and self.y%400 != 0:
				pass
			else:
				dy = dy + 1
				self.y = self.y + 1
		if self.y1%4 == 0 and self.m1 > 2:
			if self.y1%100 == 0 and self.y1%400 != 0:
				pass
			else:
				dy = dy + 1
		if dm < 0:
			while self.m > self.m1:
				if self.m in [2, 4, 6, 8, 9, 11]:
					dm = dm - 1
				elif self.m == 3:
					dm = dm + 2
				self.m = self.m - 1
		else:
			while self.m1 > self.m:
				if self.m in [1, 3, 5, 7, 8, 10]:
					dm = dm + 1
				elif self.m == 2:
					dm = dm - 2
				self.m = self.m + 1
		while self. y1 > self.y:
			if self.y%4 == 0:
				dy = dy + 1
			self.y = self.y + 1
		res = dd + dm + dy
		print("%d day(s)"%res)
def bef_or_not(d, m, y, d1, m1, y1):
	if y1 > y:
		return "bef"
	elif y1 < y:
		return "lat"
	else:
		if m1 > m:
			return "bef"
		elif m1 < m:
			return "lat"
		else:
			if d1 > d:
				return "bef"
			elif d1 < d:
				return "lat"
			else:
				return "bef"
e = "The dates you have just entered are not valid, please try again!"
while True:
	print("Please input the date here:")
	print("Note: you must put the date which happens before at the first place!")
	d = int(input("Date: "))
	m = int(input("Month: "))
	y = int(input("Year: "))
	print("and the second dates:")
	d1 = int(input("Date: "))
	m1 = int(input("Month: "))
	y1 = int(input("Year: "))
	if bef_or_not(d, m, y, d1, m1, y1) == "lat":
		print(e)
		continue
	else:
		break
c1 = Counter(d, m, y, d1, m1, y1)
c1.count()
