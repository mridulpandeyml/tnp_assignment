def countFreq(arr):
    count={}
    ans=[]
    for num in arr:
        if num not in count:
            count[num]=1
        else:
            count[num]+=1
        
    for num in arr:
        if count[num]>0:
            ans.append([num,count[num]])
            count[num]=0
    return ans

arr=[1,2,2,2,4,5,6,6,6,4,2]
print(countFreq(arr))