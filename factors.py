def factor(n):
	if(n == 0):
		print("Every number is a factor of 0")
	else:
		fact = []
		c = 0
		for i in range(1, abs(n)+1):
			if(n % i == 0):
				fact.append(str(i))
				c = c+1
		if(c == 2):
			print(n,"is a prime number")
		print("Factor of", n ,"is :", ",".join(fact))
num = int(input())
factor(num)