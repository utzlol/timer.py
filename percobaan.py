import time

a = 243532
z = 0
 

while type(a) and type(z) == int:
	b = a/3
	b = str(b)
	b = b.split('.')[1]
	if b[:1] == '0' and len(str(b)) == 1:
		print(a)
		print("opsi pertama")
		break
	
	else:
		print(f"{a} and {z}")
		print('proses')
		a = int(a) - 1
		z = z + 1
#		time.sleep(1)
else:
	print("Only input number!")
