def google(l,k):
	i=0
	b=[]
	while i<len(l):	
		a=i+1
		while a<len(l):
			b.append(l[i]+l[a])
			a+=1
		i+=1
	for r in range(len(b)):
		if b[r]==k:
			print("True")
			break
	print("Sorry")	
	
                


l=[10, 15, 3, 7]
google(l,122)
