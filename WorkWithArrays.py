# --coding:utf-8--
import os
import array

os.system("cls")
print("Input a count of elements in array")
nElems = int(input())
iArray = array.array('i')
for i in range(nElems):
    print(f"Input an element N {i+1}")
    nElem = int(input())
    iArray.append(nElem)

for i in range(nElems):    
    print(f"{iArray[i]} ", end="")