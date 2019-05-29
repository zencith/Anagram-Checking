def checkOff(s1,s2_list):
    cnt=0
    if len(s1)!=len(s2_list):
        return False;
        
    for i in range(0,len(s1)):
        for j in range(0, len(s1)):
            if s1[i]==s2_list[j]:
                cnt = cnt + 1
                s2_list[j]= 1 '''If match, will change the list values with 1'''
            
    if cnt == len(s1):
        return True
    else:
        s2_list[i]='None'
    
str1 = "listen"
str2 = "silent"
li = list(str2)
print(checkOff(str1,li))
print(li)


def sortedCheck(s1,s2):
    if len(s1)!=len(s2):
        return False
    for i in range(0,len(s1)):
        if s1[i]==s2[i]:
            return True
        else:
            return False
    
str1 = "listen"
str2 = "silent"
sortStr1 = sorted(str1)
sortStr2 = sorted(str2)
print(sortedCheck(sortStr1,sortStr2))
            

from collections import Counter 
  
def cntCheck(s1,s2): 
    return Counter(s1) == Counter(s2) 
  
if __name__ == "__main__": 
    str1 = 'listen'
    str2 = 'silent'
    print(cntCheck(str1, str2))
        
    
    



