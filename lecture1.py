import numpy as np
vector=np.array([1,2.5,3])#向量
vector2=np.array([1,2,3])
matrix=np.array([[1,0,0],[0,2,0],[1,0,1]])#矩阵
print(matrix)
print(vector)
print(matrix@vector)#矩阵与向量相乘
print(np.dot(vector,vector2))#向量之间点乘
print(np.cross(vector,vector2))#寻找垂直于这两个向量的向量
print(np.linalg.solve(matrix,vector))#寻找x使Ax=a
a=np.array([1,2.5,3],dtype="float32")
print(a)

a_random=np.random.rand(4,4)#5*5随机矩阵
print(a_random)

a_ones=np.ones(4)#长度为4的1向量
print(a_ones)

a_zeros=np.zeros((3,4))#3*4的零矩阵
print(a_zeros)

a_empty=np.empty(10,dtype="int64")
print(a_empty)

a_range=np.arange(4,10)#向量的值为4-10
print(a_range)

a_vector=np.random.rand(4)
print(a_vector)
print(a_vector@a_ones)#向量点乘可以用@

print(a_random@a_random)#矩阵相乘可以用@

print(a_random@a_ones)#向量矩阵相乘也可以用@

print(a_vector[1:4])#第1-4个数（共3个）
print(a_vector[0:3:2])#第0-3个数（共3个），间隔为2

print(a_random)
print(a_random[1,2:4])#第一行第2-4列的数（两个）
a_random[0,0]=1#使第0行第0列的值为0
print(a_random)