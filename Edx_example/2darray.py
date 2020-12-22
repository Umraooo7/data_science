#numpy 2D array
import numpy as np
import matplotlib.pyplot as plt

#create a list:
a = [[11,12,13],[21,22,23],[31,32,33]]
#to covert into a numpy array
A = np.array(a)
#print("Numpy array is:  \n",A)

print("numpy array dimension: ",A.ndim)
print("shape of array: ", A.shape)
print("size of array:   ",A.size)

#access of different element
print("element in position 0,0: ",A[0][0])
print("element in postion 1,2:  ",A[1,2])
print("element in postion 1,2(same):  ",A[1][2])
print("element in postion 1,2 row:  ",A[0][0:2])

print("\n\n\n" )
#Basic operations

x = np.array([[1,2],[2,1]])
y = np.array([[1,3],[2,1]])                         #create numpy array
print("print array x: \n", x)
print("print array y: \n", y)
z = x+y
print("addition of array x and y: \n", z)
print("multiply 2 by array x: \n",2*x)
print("Harold multiplication of two array: \n",x*y)

dotP = np.dot(x,y)
#print("dot product of two array: \n", dotP)
#print("Transpose fn of above matrix: \n", dotP.T)

#error handling
#script : "python -W ignore programe.py"    otherwise
import warnings
with warnings.catch_warnings():
    warnings.warn("Let this be your last warning")
    warnings.simplefilter("ignore")




print("Cosine fn of matrix: \n", np.cos(dotP))


print("\n\n")
# create a 3D array
d3 = [[[11,[41,0]],[12,13]],[[21,22],[32,33]],[[41,42],[52,53]]]
D3 = np.array(d3)
#print("Here is three dimensional matrix:    \n",D3)
print("Dimension of new array:  ",D3.ndim)
print("shape: ",D3.shape)
print("size: ",D3.size)
print("Datatype: ",D3.dtype)
