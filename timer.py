import time

a = 0
repeat = 0
	

try:
	while True:
		print(a)
		time.sleep(1)
		a = a + 1
except:
	b = a/60
	if b == int:	
		if b >= 60:
			c = b/60
			if c == int:
				if c == 1:
					print(f"{c} hour")
				else:
					print(f"{c} hours")
			else:
				while True:
					b = b - 2
					repeat = repeat + 1
				else:
				
		else:
			if b == 1:
				print(f"{b} minute")
			else:
				print(f"{b} minute")
	else:
			
