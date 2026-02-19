
def getMinMax( arr):
    mini=float('inf')
    maxi=float('-inf')
    for i in range(len(arr)):
        mini=min(mini,arr[i])
        maxi=max(maxi,arr[i])
        
    ans=[mini,maxi]
    return ans

arr=[2,7,10,8,6,9]
print(getMinMax(arr))