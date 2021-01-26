import numpy as np

Odd=np.array([1,2,3,4,5,6,7,8,9,10])
oddnumbers=(Odd[Odd%2==1])

print(oddnumbers)