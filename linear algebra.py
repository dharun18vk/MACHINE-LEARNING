import numpy as np

m = 16

c_values = 16

x_values = np.arange(0,10) 

y_values = m * x_values + c_values

print("x   |   y")
print("------------")
for x, y in zip(x_values, y_values):
    print(f"{(x+1):2}  |  {y:3}")
