#
def firspositive(a):
    a.sort()
    i=a[0]
    j=0
    while i<=a[len(a)-1]:
          if i==0:
             i+=1
          elif i in a:
              
              i+=1
          else:
              return [i]    
    if i>a[len(a)-1]:
       return i
