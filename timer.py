import time

second = 0
minute = 0
hour = 0

while True:
	if second < 10 :
		second = f"0{second}"
	if minute < 10:
		minute = f"0{minute}"
	if hour < 10:
		hour = f"0{hour}"
	print(f"{hour}:{minute}:{second}", end='\r')
	time.sleep(1)
	second = int(second) + 1
	minute = int(minute)
	hour = int(hour)
	if second == 60:
		minute = int(minute) + 1
		second = 0
	if minute == 60:
		hour = int(hour) + 1
		minute = 0
	
