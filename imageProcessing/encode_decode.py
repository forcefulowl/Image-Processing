import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math
import numpy as np
from PIL import Image
from copy import deepcopy

with open('/Users/gavin/Desktop/im.txt', 'r') as myfile:
    str1=myfile.read().replace('\n', '')
bit = 1
arr = ''
for c in str1:
    result = bin(ord(c))[2:].zfill(8)
    if result == '100000':
        result = '0'+result
    arr = arr + result

print('arr = ', arr)


nums = math.ceil(len(arr)/bit)
remain = len(arr)%bit
print('remain = ', remain)

path1 = 'cat.jpeg'
img = mpimg.imread(path1)
newimg = deepcopy(img)
row, column, channnel = img.shape
count = 0
count1 = 0
for i in range(row):
    for j in range(column):
        for k in range(channnel):
            value = bin(img[i ,j ,k])[2:].zfill(8)
            value = value[:8-bit] + arr[count1:count1+bit]
            count1 = count1 + bit
            newimg[i, j, k] = int(value, 2)
            count = count + 1
            if count == nums:
                break
        if count == nums:
            break
    if count == nums:
        break


count2 = 0
arr2 = ''
for i in range(row):
    for j in range(column):
        for k in range(channnel):
            value = bin(newimg[i, j, k])[2:].zfill(8)
            arr2 = arr2 + value[8-bit:]
            count2 = count2 + 1
            if count2 == nums:
                break
        if count2 == nums:
            break
    if count2 == nums:
        break

if remain != 0:
    last = arr2[len(arr2)-bit:]
    last = last[len(last)-remain:]
    arr3 = arr2[:len(arr2)-bit] + last
else:
    arr3 = arr2

count = 0
flag = 0
str2 = ''
while count < len(str1):
    arr4 = ''
    arr4 = arr3[flag:flag+8]
    result2 = chr(int(arr4, 2))
    str2 = str2 + result2
    flag = flag + 8
    count = count + 1
print('str2 = ', str2)

with open("/Users/gavin/Desktop/imr.txt", "w") as text_file:
    print("{}".format(str2), file=text_file)

plt.imshow(newimg)
plt.show()

