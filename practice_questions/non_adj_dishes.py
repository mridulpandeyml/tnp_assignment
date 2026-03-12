# Problem 1: Maximum Non-Adjacent Same Dish
def max_non_adjacent_dishes(dishes):
    n=len(dishes)
    if n==0:
        return 0
    if n==1:
        return 1
    count={}
    last={}
    for i in range(n):
        if dishes[i] not in count:
            count[dishes[i]]=1
            last[dishes[i]]=i
        else:
            if last[dishes[i]]!=i-1:
                count[dishes[i]]+=1
                last[dishes[i]]=i
    most_dish=-1
    result=-1
    for i in dishes:
        if count[i]>most_dish:
            most_dish=count[i]
            result=i
    return result

dishes=[1,2,2,1,2,1,1,1,1]
print(max_non_adjacent_dishes(dishes))
