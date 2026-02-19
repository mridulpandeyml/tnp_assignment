arr=[4,3,6,5]
for i in range(len(arr)):
    for j in range(len(arr)):
        if i<len(arr)-j:
            print(arr[i:len(arr)-j])
        
    
