import numpy as np 

a = np.array(0, dtype=np.uint8)

for i in range(1025):
    b = (a + i ).astype(np.uint8)
    bint = int(a) + i 
    print(a.dtype, b, b.dtype, bint)