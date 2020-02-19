t = tuple(eval(input()))
p=()
s=''
for i in t:
	if i not in p:
		if t.count(i)>1:
			s+=(i,)
print(s)
