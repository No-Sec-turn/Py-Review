#!/usr/bin/env python
# coding: utf-8

# # 10-2. 사용자정의 함수

# In[1]:


list1 = list(range(1,11))
print(list1)


# In[2]:


list2 = [i*2 for i in list1]
list2


# In[ ]:





# In[4]:


list1 = list(range(1,11))
print(list1)


# In[7]:


list3 = [i**2 for i in list1 if i % 2 == 1]
list3


# # 10-3. 함수의 매개변수

# In[9]:


def square2(x=2, y=3):
    x = x ** 2
    y = y ** 2
    return x,y


# In[10]:


square2()


# In[11]:


square2(2)


# In[22]:


square2(2,3)


# In[ ]:





# In[13]:


def square2(x=2, y=3):
    x = x **2
    y = y **2
    return x,y


# In[14]:


square2(4,5)


# In[15]:


square2(y=5, x=4)


# In[16]:


def changeable(x, *y):
    print(x,y)


# In[17]:


changeable(1)


# In[18]:


changeable(1,2)


# In[19]:


changeable(1,2,3)


# In[20]:


changeable(1,2,3,4,5)


# In[ ]:




