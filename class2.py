import numba
import numpy as np
import matplotlib.pylab as plt
from timeit import timeit
import time

def fast_matrix_product():
    mat1 = np.random.rand(100, 100)
    mat2 = np.random.rand(100, 100)
    assert mat1.shape[1] == mat2.shape[0]
    result = []
    for c in range(mat2.shape[1]):
        column = []
        for r in range(mat1.shape[0]):
             value = 0
             value += np.dot(mat1[r],mat2[:,c]) 
             column.append(value)
        result.append(column)
    np.array(result).transpose()
t1=timeit(fast_matrix_product,number=1000)
print(t1)

@numba.njit
def fast_matrix_product():
    mat1 = np.random.rand(100, 100)
    mat2 = np.random.rand(100, 100)
    assert mat1.shape[1] == mat2.shape[0]
    result = []
    for c in range(mat2.shape[1]):
        column = []
        for r in range(mat1.shape[0]):
             value = 0
             value += np.dot(mat1[r],mat2[:,c]) 
             column.append(value)
        result.append(column)
    np.array(result).transpose()
start=time.time()
data=compute_data()
end=time.time()
print("time",end-start)

def slow_matrix_product():
    mat1 = np.random.rand(100, 100)
    mat2 = np.random.rand(100, 100)
    mat1@mat2
t3=timeit(slow_matrix_product,number=1000)
print(t3)

