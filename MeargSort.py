def Meargsort(a):
    if len(a)>1:
        mid=len(a)//2
        left=a[:mid]
        right=a[mid:]
        Meargsort(right)
        Meargsort(left)
        i,j,k=0,0,0
        while len(right)>j and len(left)>i:
            if right[j]<left[i]:
                a[k]=right[j]
                j+=1
            else:
                a[k]=left[i]
                i+=1
            k+=1
        while i<len(left):
            a[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            a[k]=right[j]
            j+=1
            k+=1
a=[10,8,9,4,2,6,1,2,1]
Meargsort(a)
print(a)
