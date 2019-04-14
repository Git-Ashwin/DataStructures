def Partition(low,high,arr):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def QuickSort(low,high,arr):
    if low<high:
        P=Partition(low,high,arr)
        QuickSort(low,P-1,arr)
        QuickSort(P+1,high,arr)

a=[9,15,14,8,3,0,5,1,1]
QuickSort(0,len(a)-1,a)
print(a)