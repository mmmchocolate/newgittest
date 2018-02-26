#matrix testing, install numpy 
import numpy as np
a , b, c, d = 2, 4, 3, 2
x = np.array(((a,b), (c, d)))
print(x)
y = np.linalg.det(x)
print(y)