#!/usr/bin/env python
# coding: utf-8

# # 12-1. 파일입력

# In[ ]:


"""
파이썬 파일 읽기 3단계
1) 파일객체 생성
 - 파일객체 = open(파일경로/파일명,모드)
2) 파일 읽기(라인단위)
 - for 변수 in 파일객체
3) 파일객체 닫기
 - 파일객체. close()
"""


# In[13]:


fr = open('./12-1. hello.txt', 'r') 
#어떠한 디렉토리에 어떤 모드로 접근할것인가
# 'r' 읽기 모드로 접근


# In[3]:


for line in fr:
    print()


# In[4]:


fr.close()


# In[ ]:


"""
1) 파일객체 생성
with open(파일경로/파일명,모드) as 파일객체
2) 파일 읽기(라인단위)
for 
"""


"""
r 읽기모드
w 쓰기모드  동일경로/파일명 존재시 overwrite (아예 덮어쓰기)
x 쓰기모드 동일 경로/파일명 존재시 error
a 쓰기모드 동일 경로/파일명 존재시 append(기존에 추가로 써짐)
+ 파일을 읽기/쓰기모드로 
"""


# In[21]:


with open('./12-1. hello.txt', 'r') as fr:
    for aaa in fr:
        print(aaa)


# # 12-2. 파일출력

# In[22]:


fw = open('./hello_write.txt','w')


# In[25]:


fw.write('Hello World Python!!!\n')
# 파일에 쓰고자하는 내용을 기록
# 출력된 22는 문자열의 길이


# In[24]:


fw.write('Welcome to Python World!!!')


# In[31]:


fw.close()


# In[32]:


with open('./hello_write.txt', 'w') as fw:
    fw.write('Hello World Python!!!\n')
    fw.write('Welcome to Python World!!!\n')


# In[35]:


with open('./hello_write.txt', 'a') as fw:
    fw.write('New line append!!!')


# # 12-3. 파일시스템

# In[36]:


import os
#os라는 모듈을 불러옴


# In[37]:


os.listdir('.')
#현재 디렉토리에 있는 여러 파일들을 불러와줌


# In[38]:


file_list = os.listdir('.')


# In[41]:


file_ipynb = [ f for f in file_list if f.endswith('.ipynb')]
# 필터링 기능
# 디렉토리 안에서 .ipynb 파일만 추출하는 법


# In[40]:


file_ipynb


# In[51]:


os.getcwd()
#현재 파일이 실행되는 경로 표기


# In[43]:


os.mkdir('test')
# makedir 의 약자 즉, 디렉토리 생성


# In[44]:


os.path.join('.', 'test')
# 파일 시스템 내 경로 처리
# 현재 OS의 파일구분자로 연결(window 형식) 리눅스는 '/'(슬래쉬)로 표기됨


# In[45]:


os.path.abspath('hello_write.txt')
#지정된 파일의 절대 경로 반환


# In[46]:


os.path.isfile('hello_write.txt')
#매개변수로 전달되는 명칭이 파일인지, 디렉토리인지 확인해주는 함수


# In[47]:


os.path.isdir('hello_write.txt')
# 해당 인자가 디렉토리인지, 파일인지 확인해주는 함수


# In[48]:


os.path.isfile('test')


# In[49]:


os.path.isdir('test')


# In[50]:


os.path.split(os.path.abspath('hello_write.txt'))


# In[ ]:




