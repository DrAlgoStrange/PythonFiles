arr=[9,7,8,6,10,2,1,4,5,10,12,6,1,10]


def mergesort(arr,first=0,last=len(arr)):
    if  first>=last:
        return
    mid=(first+last)//2
    mergesort(arr,first,mid)
    mergesort(arr,mid+1,last)
    merge(arr,first,mid,last)

def merge(arr,first,mid,last):
    l1=[]
    r=first
    l=mid+1
    while(r<=mid) and (l<=last):
        if arr[r]<arr[l]:
            l1.append(arr[r])
            r+=1
        else:
            l1.append(arr[l])
            l+=1
    while (r<=mid):
        l1.append(arr[r])
        r+=1
    while (l<=last):
        l1.append(arr[l])
        l+=1
    print(l1)
    for i in range(first,last+1):
        arr[i]=l1[i-first]
    l1=[]

mergesort(arr,0,len(arr)-1)
print(arr)