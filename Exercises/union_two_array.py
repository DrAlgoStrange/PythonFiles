"""to find the union of two array that are sorted """

def union(a,b):
    n1=len(a)
    n2=len(b)
    union_lst=[]
    i=0
    j=0
    while i<n1 and j<n2:
        if i==0 and j==0:
            if a[i]<=b[j]:
                union_lst.append(a[i])
                i+=1
            else:
                union_lst.append(b[j])
                j+=1
        else:
            if a[i]<=b[j]:
                if union_lst[-1]==a[i]:
                    i+=1
                else:
                    union_lst.append(a[i])
                    i+=1
            else:
                if union_lst[-1]==b[j]:
                    j+=1
                else:
                    union_lst.append(b[j])
                    j+=1
    while i<n1:
        if union_lst[-1]==a[i]:
            i+=1
        else:
            union_lst.append(a[i])
            i+=1
    while j<n2:
        if union_lst[-1]==b[j]:
            j+=1
        else:
            union_lst.append(b[j])
            j+=1
    return union_lst


a=[1,1,2,3,4,5,5,7]
b=[1,3,4,6,6,10]
print(union(a,b))