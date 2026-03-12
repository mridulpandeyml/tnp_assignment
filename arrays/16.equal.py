def checkEqual(self, a, b):
    a1={}
    
    for i in a:
        if i not in a1:
            a1[i]=1
        else:
            a1[i]+=1
    for i in b:
        if i not in a1:
            return False
        elif a1[i]==0:
            return False
        a1[i]-=1
    return True