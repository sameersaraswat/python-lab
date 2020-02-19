t = eval(input())
h = int(input())
for i in t:
	if h in i:
		t[i].clear()
print(t)
