a=[5,6,7,1,1,10,2,3,0]

for i in range(1,len(a)):
     M=a[i]
     while M<a[i-1] and i>0:
        a[i]=a[i-1]
        i=i-1

     a[i]=M
print(a)