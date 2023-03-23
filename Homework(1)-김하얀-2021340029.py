#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Problem2


# In[2]:


k = "k"
print(k*9, "\t", k, sep='')
for i in range(3):
    print("\t", k, "\t", k, sep='')
print("\t", k*9, sep='')
for t in range(2):
    print("\t",k,"\t", k, sep='')
print("\t", k*9, sep='')


# In[3]:


#Problem3


# In[4]:


import numpy as np
import matplotlib.pyplot as plt

def find_idx(char, txt):
    return [i for i in range(len(txt)-4) if txt[i] == char]

#재귀함수 이용
def filter(idx_list, key, txt, n=1):
    #6번 돌려지면 끝나야함
    if n==6:
        return idx_list
    #해당 숫자가 위치한 모든 인덱스를 리스트에 저장
    res = [idx for idx in idx_list if txt[idx+n]==key[n]]
    n += 1
    return filter(res, key, txt, n)

def solution():
    arr = list(np.random.randint(0, 10, size=1000000))
    txt = ''.join( str(_) for _ in arr)
    key = "340029"
    #3 스캔 -> 4스캔 -> 0스캔 ...
    idx_list = find_idx('3', txt)
    total = filter(idx_list, key, txt)
    return len(total)


# In[18]:


real=0
for i in range(100):
    real+=solution()
real /=100 # res는 real probability
print(real)
theory = 10**6/10**6 # thoery는 수학적 확률. 얼추 비슷하게 나옴
print(theory)


# In[ ]:


#Problem4


# In[19]:


import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('housing.csv')
#median_house_value” and “median_income”8, 9번째임
name = ["longitude", "latitude", "median_house_value", "median_income"]
print(data)


# In[20]:


x_data1 = data[name[2]].loc[:]
y_data1 = data[name[3]].loc[:]
plt.scatter(x_data1, y_data1, s=0.1)
plt.xlabel('median_house_value')
plt.ylabel('median_income')


# In[24]:


# 5번문제

from mpl_toolkits.mplot3d import Axes3D

x_data2 = data[name[2]].loc[:]
y_data2 = data[name[0]].loc[:]
z_data2 = data[name[1]].loc[:]


# 3D 그래프 생성
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('median_house_value')
ax.set_ylabel('longitude')
ax.set_zlabel('latitude')
ax.scatter(x_data2, y_data2, z_data2, s=0.1)
plt.show()


# In[26]:


#6번 문제
def d_m(mat1, mat2):
    #행렬의 사이즈 조사 
    m, n = np.shape(mat1)[0], np.shape(mat2)[1]
    res=np.ones((m,n))
    #해당 위치별로 나눠주기
    for i in range(m):
        for j in range(n):
            if mat1[i][j] == 0 or mat2[i][j]==0:
                continue
            res[i][j]=mat1[i][j]/mat2[i][j]
    return res

def m_mt(mat):
    #0으로 채워두고 채우기
    m, n = np.shape(mat)[0], np.shape(mat)[1]
    res=np.zeros((m,m))
    for i in range(m):
        for j in range(m):
            for t in range(n):
                res[i][j]+=mat[i][t]*mat.transpose()[t][j]               
    return res

x = list("20021121")
y = list("20213400")
mat = np.array([x,y], dtype = 'int')
a = [mat + 7, mat - 7, mat * 7, np.add(mat, mat), d_m(mat, mat)]
b = [np.multiply(mat, mat), m_mt(mat.transpose()), m_mt(mat)]
print(a)
print(b)


# In[27]:


#6번문제
class student:
    def __init__(self, name, student_number, gender, age, courses):
        self.name = name
        self.student_number = student_number
        self.gender = gender
        self.age = age
        self.courses = courses
    
    def upper_only1(self):
        self.name = self.name.lower()
        self.name = self.name[0].upper() + self.name[1:]
    
    def after_years(self, years):
        self.age +=years
    
    def del_courses(self, number):
        if number > len(self.courses):
            print("errer")
        elif number == 0:
            print("error")
        else :
            del self.courses[number-1]

student1 = student('hAyan',2021340029, 'f',22,['Reinforcement learning', 'Psychology', 'Algorithm', 'Machine Learning', 'Espanol'])
student1.upper_only1()
student1.after_years(3)
student1.del_courses(2)
print(student1.__dict__)

