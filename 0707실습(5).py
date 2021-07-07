#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip list #내장 모듈 리스트 확인 방법')


# In[ ]:


help('sys') #help() 내장함수를 이용하여 모듈 사용 도움말 확인


# In[ ]:


"""
import[모듈명]
import[모듈명]as[Alias명]
from[패키지명]import[모듈명]
from[모듈명]import[클레스명/함수명]
"""


# In[4]:


import os #여러가지 운영체제를 활용하기 위한 기본 모듈


# In[5]:


os.getcwd() #실행되는 디렉토리 위치 경로 확인방법


# In[6]:


os.listdir()


# In[ ]:





# In[7]:


import numpy as np


# In[8]:


np.absolute(-3) #절대값 계산하는 함수


# In[9]:


np.sqrt(16) #루트씌운 값 계산하는 함수


# In[ ]:





# In[10]:


from scipy import stats 
#from [패키지명] import [모듈명] 싸이파이 패키지안에 스탯츠라는 모듈을 사용하겠다!


# In[11]:


stats.hmean([1,2,3]) 


# In[21]:


stats.variation([1,2,3]) #분산값 계산하는 함수


# In[14]:


from datetime import datetime
#from [모듈명] import [클래스명/함수명]
#datetime이라는 모듈안에 datetime이라는 클래스를 사용하는것


# In[15]:


now = datetime.now()


# In[17]:


now.year


# In[18]:


now.month


# In[ ]:


"""
o 모듈의 물리적 위치
 -파이썬에서 모듈 import시 해당 모듈의 물리적 위치 탐색 순서
    1) 현재 디렉토리
    2) 환경변수 PYTHONPATH에 지정된 경로
    3) Python이 설치된 경로 및 하위 라이브러리 디렉토리 경로
"""


# In[19]:


import sys 


# In[20]:


sys.path #import를 할때 물리적 위치를 찾는 경로를 보여줌


# # 11.3 파이썬 사용자 정의 모듈

# In[ ]:


"""
사용자 정의 모듈
현재 디렉토리에 pyprint.py로 저장
myprint.py 모듈 import 및 tap키로 함수 확인
"""


# In[23]:


import myprint


# In[24]:


hello = 'Hello World Python'


# In[ ]:





# In[25]:


myprint.print1(hello)


# In[26]:


myprint.print2(hello)


# In[31]:


from mymodule import myprint2 
#현재 디렉토리밑에 mymodule이라는 디렉토리 밑에 있는 myprint2라는 패키지를 사용하는것임.


# In[32]:


myprint2.print3(hello)


# In[33]:


myprint2.print4(hello)


# In[ ]:




