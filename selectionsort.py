import sys
a=[10,10,10,1,3,5,7,8,8]

def selectionsort(a):
 for i in range(len(a)):
   Min=a[i]
   Index=None
   for j in range(i,len(a)):
       if a[j]<Min:
           Min=a[j]
           Index=j
   if Index!=None:
      a[Index],a[i]=a[i],a[Index]
     

selectionsort(a)
print(a)