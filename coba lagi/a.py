def printDict():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	for k,v in d.items():	
		print k,v
		

printDict()
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print li
		

printList()
def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print li[:5]
		

printList()
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter(lambda x: x%2==0, li)
print evenNumbers
li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = map(lambda x: x**2, li)
print squaredNumbers
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print evenNumbers
evenNumbers = map(lambda x:x**2, filter(lambda x: x%2==0, range(1,21)))
print evenNumbers
apa = map(lambda x:x/5, filter(lambda x:x%3==0, range(1,101)))
print apa
