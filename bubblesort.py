a=[10,10,20,4,2,7,6,3]
def bubblesort(a):
 for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
bubblesort(a)
print(a)

