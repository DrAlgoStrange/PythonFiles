def merge_sort(nums,start,end,cn=0,l_cn=0):
            if start>=end:
                return (cn,l_cn)
            mid=(start+end)//2
            cn,l_cn=merge_sort(nums,start,mid,cn,l_cn)
            cn,l_cn=merge_sort(nums,mid+1,end,cn,l_cn)
            cn,l_cn=merge_nums(nums,start,mid,end,cn,l_cn)
            return (cn,l_cn)
def merge_nums(nums,start,mid,end,cn,l_cn):
            result=[]
            i=start
            j=mid+1
            while (i<=mid and j<=end):
                if nums[i]<=nums[j]:
                    result.append(nums[i])
                    i+=1
                    
                else:
                    result.append(nums[j])
                    j+=1
                    cn+=(mid-i)+1
            while i<=mid:
                result.append(nums[i])
                i+=1
            while j<=end:
                result.append(nums[j])
                j+=1
            for i in range(start,end+1):
                nums[i]=result[i-start]
            return (cn,l_cn)

nums=[1,2,3,5,4]
nums_duplicate = nums[:]
length=len(nums_duplicate)
global_ans,local_ans=merge_sort(nums_duplicate,0,length-1,0,0)
print(global_ans==local_ans)