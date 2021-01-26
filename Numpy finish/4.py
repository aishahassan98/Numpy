import numpy as np

Odd=np.array([1,2,3,4,5,6,7,8,9,10])
(Odd[Odd%2==1])= -1
#This function looks at the remainder iif the remainder is equal to 1 \
#Then it is replaced with -1
print(Odd)


