# Part 2 of the Python Review lab.
'''
def encode(x, y):
	if y<1 or y>250 or x<500 or x>1000:
		print("invalid input:outside range")
		return None
	return x*y
'''

def isprime(num):
	for i in range(2,num):
		if num%i==0:
			return False
	return False


def encode(x,y):
	while  not isprime(x):
		x+=1
	while not isprime(y):
		y+=1
	if y<1 or y>250 or x<500 or x>1000:
		print("invalid input:outside range")
		return None
	return x*y

isprime(2,2)


def decode(coded_message):
	for y in range(2,250):
		if not isprime(y):
			continue
		if coded_message%y==0:
			x=coded_message//y
			if isprime(x) and  500<x<1000:
				return (x,y)
				
	# for x in range(500,1001):
	# 	y=coded_message/x
	# 	if coded_message%y==0:
	# 		if isprime(x) and isprime(y) and 1<y<250:
	# 			return x+","+y
