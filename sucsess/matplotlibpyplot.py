import matplotlib.pyplot as plt 
import numpy as np 
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x,y)
plt.show()


x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('sin(x)')
plt.title('График функции sin(x)')
plt.grid(True)
plt.show()