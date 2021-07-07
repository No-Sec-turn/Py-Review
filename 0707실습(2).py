#!/usr/bin/env python
# coding: utf-8

# #08-1 비교 논리

# In[1]:


x,y = 10,5    # x = 10; y=10 ;는 줄바꿈 표시


# In[2]:


x == y


# In[3]:


x != y


# In[4]:


x > y


# In[5]:


x<y


# In[6]:


x >= y


# In[8]:


x <= y


# In[ ]:





# In[9]:


x = True; y = False


# In[10]:


x and y


# In[11]:


x or y


# In[12]:


not x


# # 08-2. 조건문

# In[13]:


x,y = 10,5


# In[14]:


if x >y:
    print('x가 y보다 큽니다.')


# In[15]:


x,y = 5,10


# In[17]:


if x>y:
    print('x가 y보다 큽니다.')
else:
    print('x가 y보다 작습니다.')


# In[18]:


x,y = 10,10


# In[19]:


if x > y:
    print('x가 y보다 큽니다.')
elif x == y:
    print('x와 y가 같습니다.')
elif x < y:
    print('x가 y보다 작습니다.')


# In[20]:


score = 90


# In[21]:


if score >= 90:
    print('A학점입니다.')
elif score >= 80:
    print('B학점입니다.')
elif score >= 70:
    print('C학점입니다.')
elif score >= 60:
    print('D학점입니다.')
else:
    print('F학점입니다.')


# In[24]:


a = True
if a:
    print("a는 True입니다.")
    print("True End...")
else:
    print("a는 False입니다.")
print('False End...')


# # 08-3. 중첩 복합 조건문

# In[27]:


a = True
x,y = 5,10


# In[28]:


if a -- True:
    print('a는 True입니다.')
    if x>y:
        print('x가 y보다 큽니다.')
    else:
        print('x가 y보다 작습니다.')
else:
    print('a는 False입니다.')


# In[38]:


나이 = 30
회원 = True


# In[30]:


입장료 = 0


# In[32]:


if 회원:
    if 나이 >6 and 나이 <= 13:
        입장료 = 2500
    elif 나이 > 14 and 나이 <= 59:
        입장료 = 5000
else:
    if 나이 > 6 and 나이 <= 13:
        입장료 = 5000
    elif 나이 > 14 and 나이 <= 59:
        입장료 = 10000
        
print(f'입장료는 {입장료:,}원 입니다.')


# In[33]:


입장료 = 0


# In[39]:


if 나이 <= 6 or 나이 >=60:
    입장료 = 0
elif 나이 > 6 and 나이 <= 13:
    입장료 = 5000
elif 나이 > 14 and 나이 <= 59:
    입장료 = 10000
    
if 회원:
    입장료 = int(입장료 * 0.5)

print(f'입장료는 {입장료:,}원 입니다.')


# In[ ]:




