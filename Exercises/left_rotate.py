def left_rotate(arr,times=1):
    if times==0:
        return
    else:
        fst_element=arr[0]
        for i in range(0,len(arr)-1):
            arr[i]=arr[i+1]
        arr.pop()
        arr.append(fst_element)
        print(arr)
        times=times-1
        left_rotate(arr,times)



left_rotate([2,5,1,6,8],10)
