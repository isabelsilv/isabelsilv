n = int(input("type a numbers: "))
m = int(input("type another number: "))

i=m
z = 1
list = []
list2 = []
j = 0
a = n*m
print(a)

while z<=n :
	print("%(z)d| %(i)d" %{"z":z,"i":i})
	z = z*2
	i = m*z
	list.append(z)
	list2.append(i)
print(list)
print(list2)
  
	
	
		