#!/usr/bin/env python
# coding: utf-8

# In[25]:


word='abcdeff ghh ijjj kk'
word1=set(word.replace(' ',''))
lst=[]
for i in word1:
    if word.count(i)>1:
        lst.append(i)
lst.sort()
print(lst)  
       


# In[66]:


letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
        's','t','u','v','w','x','y','z']

word='abcabcd'
word=word.replace(' ','')
lst=[]
cnt=0
while cnt< len(word):
    num=word.count(word[cnt],0,cnt+1)
    cnt+=1
    lst.append(num)
word=list(word)
for i in range (0,len(lst)):
    if lst[i]>1:
        word[i] =letter[letter.index(word[i])+lst[i]-1]
''.join(word)


# In[90]:


def counters(s):
    counter_dic = {}
    result = ''
    #alpha_list = []
    for char in s:
	if char==" ":
	result+=char
        elif char not in counter_dic:
            result+=char
            counter_dic[char] = 1
            #alpha_list.append(char)
            
        else:
            counter_dic[char]+=1
            char = chr(ord(char)+(counter_dic[char]-1))
            result+=char
            
    print(result)      
            
counters('daabc abcddk  ')


# In[80]:


def change_char(text):
    dict_t={}
    result=''
    ls=[]
    for char in text:
        if char not in result:
            result+=char
            dict_t[char]=1
        else:
            dict_t[char]+=1
            char=chr(ord(char)+dict_t[char]-1)
            result+=char
    print(result)
    
change_char('abcabcd')


# In[ ]:




