def second_Largest(arr):
    if arr[0]>arr[1]:
        first=arr[0]
        second=arr[1]
    else:
        second=arr[0]
        first=arr[1]
    for i in range(2,len(arr)):
        if arr[i]>=first:
            second=first
            first=arr[i]
        elif arr[i]<first and arr[i]>second:
            second=arr[i]
    return second

arr=[2,7,10,8,6,9]
print(second_Largest(arr))