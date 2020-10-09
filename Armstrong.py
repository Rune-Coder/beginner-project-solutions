num = int(input("Enter a number: "))
dig = len(str(num))#number of digits
sum = 0
copy = num
while copy > 0:
   digit = copy % 10
   sum += digit ** dig
   copy //= 10
# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")