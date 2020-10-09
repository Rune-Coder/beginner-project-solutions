def loop_fibo(n):
	n1, n2 = 0, 1	
	print("Fibonacci sequence by loop:")
	for i  in range (n):
		print(n1)
		nth = n1+n2
		n1 = n2
		n2 = nth
def recur_fibo(n):
	if n <= 1:
		return n
	else:
		return(recur_fibo(n-1) + recur_fibo(n-2))
nterms = int(input("How many terms?\n"))
if nterms <= 0:
	print("Please enter a positive integer")
elif nterms == 1:
	print("Fibonacci sequence upto",n,":")
	print(n1)
else:
	loop_fibo(nterms)
	print("Fibonacci sequence by recursion:")
	for i in range(nterms):
   	 print(recur_fibo(i))