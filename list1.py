k = list(map(int,input().split()))
b = []
for i in k:
	if i not in b:
		b.append(i)
print(*b,sep='*')
