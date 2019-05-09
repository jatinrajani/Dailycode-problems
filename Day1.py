def google(l,k):
	i=0
	b=[]
	while i<len(l):	
		a=i+1
		while a<len(l):
			b.append(l[i]+l[a])
			a+=1
		i+=1
	for r in b:
		if r==k:
			print("True")
			break
l=[10, 15, 3, 7]
google(l,17)
