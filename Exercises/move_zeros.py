def mov(arr):
    temp=[]
    for i in arr:
        if i!=0:
            temp.append(i)
    for i in range(0,len(arr)):
        if i<len(temp):
            arr[i]=temp[i]
        else:
            arr[i]=0


l1=[1,0,6,7,0,9,0,7,2,3,0,5]
mov(l1)
print(l1)