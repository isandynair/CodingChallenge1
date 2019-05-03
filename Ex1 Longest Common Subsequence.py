#!/usr/bin/env python
# coding: utf-8

# In[1]:


def lcs(s1, s2):
    
#initialize a 2D empty matrix
    
    matrix = [["" for x in range(len(s2))] for x in range(len(s1))]

# i -->row    j -->col

    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    matrix[i][j] = s1[i]                 
                else:
                    matrix[i][j] = matrix[i-1][j-1] + s1[i] #pasting the diagonally opposite value + matched string value                   
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], key=len) #comparing length of top and adjacent matrix value

    cs = matrix[-1][-1] #final row & col value

    print("The longest common subsequence is ")
    
    return cs

s1=input("First string? ")
s2=input("Second string? ")

s1=s1.lower()
s2=s2.lower()

if(len(s1)==0) and (len(s2)==0):
    
    print("Please enter something")

elif(len(s1)==0) or (len(s2)==0):

    if(len(s1)>len(s2)):
        
        print("The longest common subsequence is "+s1)
        
    else:
        print("The longest common subsequence is "+s2)
        
else:    
    print(lcs(s1, s2))


# In[ ]:




