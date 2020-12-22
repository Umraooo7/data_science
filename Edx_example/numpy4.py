#more excercise
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

a = np.array([0,1,2,3,4])
print(a)
print(a.size)               #size of array
print(a.ndim)
print(a.shape)              #size of numpy array

a = np.array([1,-1,1,-1])
mean = a.mean()
print("Mean of array: ",mean)                 #mean of array

print("standard deviation: ",a.std())           #sd of array

b = np.array([1,-2,4,5])
print("Max value of array: ",b.max())           #max of array
print("Min. value of B: ", b.min())             #min of array

#vector or scaler operations
u = np.array([1,2])
print(u)
v = np.array([3,1])
print(v)

print("Addition of vector: ", u + v)            #addition of vector
print("Multiplication of vector: ", 2*u)        #mult of vector
print("Multiplication of two vectors: ", v*u)  #mult of two vector

print("Dot product of vector: ", np.dot(u,v))   #Dot product
print("Scaler addition of: ", u + 1)            #scaler addition
print("Value of pi: ", np.pi)

x = np.array([0,np.pi/2,np.pi])
print("New array x: ",x)
y = np.sin(x)
print("Sine funtion of x: ",y)                  #sine function of x

#Linespace examples
print("linespace: ", np.linspace(-2,2,num=9))   #linespace function

z = np.linspace(0, 2*np.pi, num=100)
print(z)

z1 = np.sin(z)
print(z1)

plt.plot(z,z1)
plt.show()                                      #to show the graph
