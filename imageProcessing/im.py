import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image
from copy import deepcopy


str1 = 'Image processing is a good course'
arr = ''
for c in str1:
    result = bin(ord(c))[2:]
    if result == '100000':
        result = '0'+result
    arr = arr + result

print('arr = ', arr)

length = len(str1)

path1 = '/home/gavin/Desktop/B2DBy.jpg'
img = mpimg.imread(path1)

newimg = deepcopy(img)
count1 = 0
row, column, channel = img.shape
for i in range(row):
    for j in range(column):
        newimg[i, j] = img[i, j] + int(arr[count1])
        count1 = count1 + 1
        if count1 == len(arr):
            break
    if count1 == len(arr):
        break

count2 = 0
arr3 = ''
row, column, channel = img.shape
for i in range(row):
    for j in range(column):
        result = (newimg[i, j, 0] - img[i, j, 0])
        arr3 = arr3 + str(result)
        count2 = count2 + 1
        if count2 == len(arr):
            break
    if count2 == len(arr):
        break
print('arr3 = ', arr3)


count = 0
flag = 0
str2 = ''
while count < len(str1):
    arr2 = ''
    arr2 = arr3[flag:flag+7]
    result2 = chr(int(arr2, 2))
    str2 = str2 + result2
    flag = flag + 7
    count = count + 1
print('str2 = ', str2)

# plt.imshow(img)
# plt.imshow(newimg)
# plt.show()
