
n = int(input("type a numbers: "))
m = int(input("type another number: "))

i=m
z = 1
list = []
list2 = []
j = 0
a = n*m
print(a)

while n>=z :
	list.append(z)
	list2.append(i)
	print("%(z)d| %(i)d" %{"z":z,"i":i})
	z*=2
	i = m*z

list = list[::-1]
list2 = list2[::-1]
print(list)
print(list2)
list1=[]
for num in list2:
	print(a)
	while num<=a:
		a = a - num
		list1.append(num)

print(list1)
count = 0
for s in list1:
	count += s
print(count)		

print()


		
		
	


		
	
	
		