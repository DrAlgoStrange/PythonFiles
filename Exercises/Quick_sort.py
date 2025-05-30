arr=[23,4,56,666,1,2,99,6,6,2]

def quick_sort(arr,first=0,last=len(arr)-1):
    if first>=last:
        return
    partion_ind=q_sort(arr,first,last)
    quick_sort(arr,first,partion_ind-1)
    quick_sort(arr,partion_ind+1,last)

def q_sort(arr,first,last):
    pivot=arr[first]
    i=first
    j=last
    while i<j:
        while i<=last and arr[i]<=pivot:
            i+=1
        while j>=first and arr[j]>pivot:
            j-=1
        if j>i:
            arr[i],arr[j]=arr[j],arr[i]
    arr[j],arr[first]=arr[first],arr[j]
    return j

quick_sort(arr)
print(arr)