#!/usr/bin/env python
# coding: utf-8

# #07-1. 셋

# In[1]:


set1= {'A', 'B','C', 'D', 'E', 'F', 'B'}
set1


# In[2]:


set1[0] #set은 인덱스 사용 불가


# In[3]:


set1[:5] #set은 슬라이싱 사용불가


# In[10]:


set1.add('a')
set1


# In[11]:


set1.add('A')
set1


# In[12]:


set1.remove('a')
set1


# In[13]:


set1.pop()
set1


# In[14]:


중간고사 = {
    "수학": 100,
    "영어": 90,
}
중간고사


# In[15]:


중간고사['국어'] = 85


# In[16]:


중간고사


# In[17]:


중간고사['영어']


# In[20]:


list(중간고사.keys())


# In[21]:


list(중간고사.values())


# In[22]:


중간고사.items()


# #07-2 셋의 집합연산

# In[23]:


set1 = {'A', 'B', 'C', 'D','E', 'F'}
set2 = {'B', 'D', 'G', 'H'}


# In[24]:


set1 & set2 #교집합 요소 추출


# In[25]:


set1.intersection(set2) # & 와 같은 기능 


# In[26]:


set1 | set2 #합집합


# In[27]:


set1.union(set2) # | 와 같음


# In[28]:


set1 - set2 #차집합


# In[31]:


set1.difference(set2) # - 와 같음


# In[32]:


set1 ^ set2 # 교집합을 제외한 나머지를 합해서 보여줌


# In[33]:


set1.symmetric_difference(set2) # ^와 같음


# #07-3 딕셔너리

# In[46]:


중간고사 = {
    "수학" : 100,
    "영어" : 90,
}
중간고사


# In[47]:


중간고사['국어'] = 85
중간고사 #새로운 element 추가


# In[48]:


중간고사['영어']


# In[50]:


중간고사['영어'] = 95
중간고사 #특정 key값을 변경


# In[52]:


list(중간고사.keys()) #해당 dic의 key값만 추출


# In[53]:


list(중간고사.values()) #해당 dic의 item만 추출


# In[54]:


중간고사.items() #key와 val을 동시에 추출


# In[55]:


중간고사.pop('국어') #원소 삭제


# In[56]:


중간고사


# In[ ]:




