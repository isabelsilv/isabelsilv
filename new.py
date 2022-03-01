print("Type a number: ")
n = int(input());
list = []

while n!=1:

	if (n%2==0):
		n = n/2
		list.append(n)
		print(n)
	elif(n==1):
		n= (n*3)+1
	else:
		n = (n*3)+1
		print(n)		