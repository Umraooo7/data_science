#use of numpy
import numpy as np
a = [1,2,3,4,5]
x = np.array(a)     #function type
print(x)
print(type(x))      #type of function
z = x.shape         #space in array
print(z)

print(x.dtype)
print(x.mean())     #mean value of array


k = np.array([1,-1])*np.array([1,1])    #muliplicaton of array
print("prodct of array: ",k)

j = np.dot(np.array([1,-1]),np.array([1,1]))
print("Dot product of array: ",j)            #dot product
