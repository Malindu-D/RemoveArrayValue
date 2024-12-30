from array import *


Arr = array('i', [2,3,6,8,1])
Arr2 = array('i', [])

for i in range(len(Arr)):
    if i != 2:
        Arr2.append(Arr[i])

print("Before Remove index of 2:", end=" ")
for e in Arr:
    print(e, end=" ")
print()

print("After Remove index of 2 :", end=" ")
for e in Arr2:
    print(e, end=" ")
print()