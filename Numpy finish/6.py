import numpy as np

a = np.arange(1,10).reshape (3,3)
b = np.arange(11,20).reshape (3,3)
print(a,b)
ans =np.dot(a,b)
print(ans)
anz=np.sum(ans)