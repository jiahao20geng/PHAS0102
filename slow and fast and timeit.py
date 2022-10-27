import numpy as np
def slow_matrix_product(mat,vec):
    assert mat.shape[1]==vec.shape[0]
    result=[]
    for r in range(mat.shape[0]):
        value=0
        for c in range(mat.shape[1]):
            value+=mat[r,c]*vec[c]
        result.append(value)
    return np.array(result)
mat = np.random.rand(3, 3)
vec= np.random.rand(3)
print(slow_matrix_product(mat, vec))
print(mat @ vec)

def fast_matrix_product(mat,vec):
    assert mat.shape[1]==vec.shape[0]
    result=[]
    for r in range(mat.shape[0]):
        value=0
        value+=np.dot(mat[r],vec)#!!!!!!difference
        result.append(value)
    return np.array(result)

from timeit import timeit
def slow_matrix_product():
    mat = np.random.rand(100, 100)
    vec= np.random.rand(100)
    assert mat.shape[1]==vec.shape[0]
    result=[]
    for r in range(mat.shape[0]):
        value=0
        for c in range(mat.shape[1]):
            value+=mat[r,c]*vec[c]
        result.append(value)
    np.array(result)
t=timeit(slow_matrix_product,number=100)
print(t)

def fast_matrix_product():
    mat = np.random.rand(100, 100)
    vec= np.random.rand(100)
    assert mat.shape[1]==vec.shape[0]
    result=[]
    for r in range(mat.shape[0]):
        value=0
        value+=np.dot(mat[r],vec)
        result.append(value)
    np.array(result)
t2=timeit(fast_matrix_product,number=1000)
print(t2)

def veryfast_matrix_product():
    mat = np.random.rand(100, 100)
    vec= np.random.rand(100)
    mat@vec

t3=timeit(veryfast_matrix_product,number=1000)
print(t3)