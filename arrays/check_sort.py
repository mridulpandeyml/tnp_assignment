def check(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return False
    
    return True

arr=[1,2,3,4,5,6,1]
print(check(arr))