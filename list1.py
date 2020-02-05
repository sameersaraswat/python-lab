l = []
while 1:
	item = input("Enter item")
	l.append(item)
	
	n = input('do you want continue')
	if n.lower()=='n':
		break
l.sort(reverse=True,key=max)
print(l)
