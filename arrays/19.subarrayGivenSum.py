def subarraySum( arr, target):
    total=0
    start=0
    for i in range(len(arr)):
        total+=arr[i]
        if total==target:
            return [start+1,i+1]
        while total>target:
            total-=arr[start]
            start+=1
            if total==target:
                return [start+1,i+1]
        
    return [-1]    