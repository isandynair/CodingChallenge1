#!/usr/bin/env python
# coding: utf-8

# In[17]:


#to check sequential pattern of string matches with pattern
def substr(string, pat):
    x = pat
    str_list = []
    
    if isMatch(string, x):
        return True

    for j in range(2, len(x)):
        for i in range(len(x)-j+1):
            if isMatch(string, x[i:i+j]):
                return True
    return False

#to remove two consecutive stars & replace with single star
def star(char, s):
    while char * 2 in s:
        s = s.replace(char * 2, char)
    return s

#dynamic programming
def isMatch(s, p):
    p=star("*",p)
    m = [[False for x in range(len(p)+1)] for y in range(len(s)+1)]
    m[0][0]=True
             
   
    for i in range(1,len(s)+1):
        for j in range(1,len(p)+1):
            
            if (p[j-1]==s[i-1]) or (p[j-1]=="."):
                m[i][j]=m[i-1][j-1]
                
            elif (p[j-1]=="*"):
                
                if (p[j-2]==".") or (p[j-2]==s[i-1]):
                    m[i][j]= m[i-1][j] | m[i][j-1]
                    
            else:
                m[i][j]=False         
    
    return m[len(s)][len(p)]

s=input("String? ")
    
p=input("Pattern? ")
    
print(substr(s,p))


# In[ ]:




