def product(a):
    product=1
    i=0
    while i<len(a):
        product=product*a[i]
        i+=1
    return product

def insertlist(a):
    c=[]
    for i in range(len(a)):
        c.append(a[i])
    return c


def uberprogram(a):
    i=0
    b=[]
    c=insertlist(a)
    
    while i<len(c):
       c[i]=1
       b.append(product(c))
       
       i+=1
       c=insertlist(a)
       
    return b


#input a=[1,2,3,4,5]
#output b=[120, 60, 40, 30, 24]
