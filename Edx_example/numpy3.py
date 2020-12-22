#Python lists
#Create Python list
import numpy as np

a = ["0",1,"Two",3,4.0,"Five"]
print("a[0]:    ",a[0])
print("a[1]:    ",a[1])
#print("a[2]:    ",a[2])
#print("a[3]:    ",a[3])
#print("a[4]:    ",a[4])
#print("a[5]:    ",a[5])

b = np.array([0,1,2,3,4])
print(b)
print("b[0]:    ",b[0])
print("b[1]:    ",b[1])

print(type(b))      #data type of b
print(b.dtype)

c = np.array([20,1,2,3,4])
print(c)            #create numpy array

c[0] = 100          #assign value in array
print("c[0]: ",c[0])

d = c[1:3]
print(d)            #slicing array

c[2:3] = 300, 400
print("New array:   ", c)
