def reverseArray(arr):
    start=0
    end=len(arr)-1
    while start<=end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr
def leaders(arr):
    n=len(arr)
    leader=0
    ans=[]
    for i in range (0,n):
        if arr[n-i-1]>=leader:
            leader=arr[n-i-1]
            ans.append(leader)
    reverseArray(ans)
    
    return ans

arr = [10, 4, 2, 4, 1]
print(leaders(arr))