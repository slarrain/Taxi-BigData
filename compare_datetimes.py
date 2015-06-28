from datetime import datetime
def compare(datetime1,datetime2):
	hour1 = datetime.strptime(datetime1, "%Y-%m-%d %H:%M:%S").hour
	hour2 = datetime.strptime(datetime2, "%Y-%m-%d %H:%M:%S").hour
	day1 = datetime.strptime(datetime1, "%Y-%m-%d %H:%M:%S").weekday()
	day2 = datetime.strptime(datetime2, "%Y-%m-%d %H:%M:%S").weekday()
	if hour1 >=5 and hour1 < 11:
		period1 = 0
	elif hour1>=11 and hour1 <16:
		period1 =1
	elif hour1>=16 and hour1 <20:
		period1 = 2
	else:
		period1 = 3

	if hour2 >=5 and hour2 < 11:
		period2 = 0
	elif hour2>=11 and hour2 <16:
		period2 =1
	elif hour2>=16 and hour2 <20:
		period2 = 2
	else:
		period2 = 3

	if (day1>=4) and (day2>=4):
		if period1 == period2:
			return True
	elif (day1>=0) and (day1<4) and (day2>=0) and (day2<4):
		if period1 == period2:
			return True
	return False
