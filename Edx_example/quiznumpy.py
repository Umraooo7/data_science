#quiz numpy
import numpy as np
import matplotlib.pyplot as plt


a = np.array([-1,1])
b = np.array([1,1])

def Plotvec2(a,b):
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

Plotvec2(a,b)
print("This is dot product: ", np.dot(a,b))
