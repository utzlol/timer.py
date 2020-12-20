import time

a = 19
z = 0
 

if ".0" in str(a/5) and len(str(a/5)) == 3:
	print(a)
	print("opsi pertama")
	
else:
	while ".0" not in str(a/5) and len(str(a/5)) != 3:
		print(a/5)
		print(".0" in str(a/5) and len(str(a/5)) == 3)
		print(f"{a} and {z}")
		print(f"{a}/5")
		a = a - 1
		z = z + 1
		time.sleep(2)
	else:
		print(f"Jadi {a} + {z}")
		print("ini else terakhir")