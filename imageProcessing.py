import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from copy import deepcopy
import math
import random


def rgbToGray(img):
    row, column, channel = img.shape
    for i in range(row):
        for j in range(column):
            # print('row = ',i,'column = ',j)
            avglist = img[i,j]
            avg = int(avglist[0]*0.299 + avglist[1]*0.587 + avglist[2]*0.114)
            img[i,j] = [avg,avg,avg]
    return img


def smooth_avg(img):
    row, column, channel = img.shape
    img1 = deepcopy(img)
    for i in range(1,row-1):
        for j in range(1,column-1):
            img[i,j,0] = math.floor(img1[i,j,0]*0.2)+math.floor(img1[i-1,j,0]*0.2)+math.floor(img1[i,j-1,0]*0.2)+math.floor(img1[i,j+1,0]*0.2)+math.floor(img1[i+1,j,0]*0.2)
            #img[i,j,1] = math.floor(img1[i,j,1]*0.2)+math.floor(img1[i-1,j,1]*0.2)+math.floor(img1[i,j-1,1]*0.2)+math.floor(img1[i,j+1,1]*0.2)+math.floor(img1[i+1,j,1]*0.2)
            #img[i,j,2] = math.floor(img1[i,j,2]*0.2)+math.floor(img1[i-1,j,2]*0.2)+math.floor(img1[i,j-1,2]*0.2)+math.floor(img1[i,j+1,2]*0.2)+math.floor(img1[i+1,j,2]*0.2)
            img[i,j,1] = img[i,j,2] = img[i,j,0]
    return img


def smooth_median(img):
    row, column, channel = img.shape
    img1 = deepcopy(img)
    for i in range(1,row-1):
        for j in range(1,column-1):
            list = [img1[i-1,j-1,0],img1[i-1,j,0],img1[i-1,j+1,0],img1[i,j-1,0],img1[i,j,0],img1[i,j+1,0],img1[i+1,j-1,0],img1[i+1,j,0],img1[i+1,j+1,0]]
            list.sort()
            img[i,j,0] = img[i,j,1] = img[i,j,2] = list[4]
    return img

def salt_pepper(img):
    row, column, channel = img.shape
    nums = int((row * column)*0.1)
    for i in range(nums):
        num1 = random.randint(0,row-1)
        num2 = random.randint(0,column-1)
        if img[num1,num2,0]>=100:
            img[num1,num2] = [0,0,0]
        else:
            img[num1,num2] = [255,255,255]
    return img

def binary_thresholding(img, thresholding):
    row, column, channel = img.shape
    for i in range(row):
        for j in range(column):
            if img[i,j,0] >= thresholding:
                img[i,j] = [255,255,255]
            else:
                img[i,j] = [0,0,0]
    return img


def binary_ptile(img,x):
    row, column, channel = img.shape
    nums = row * column
    list = []
    for i in range(row):
        for j in range(column):
            list.append(img[i,j,0])
    list.sort()
    p = list[int((nums-1)*(1-x*0.01))]
    for i in range(row):
        for j in range(column):
            if img[i,j,0] >= p:
                img[i,j] = [255,255,255]
            else:
                img[i,j] = [0,0,0]
    return img


def calculateT(img,thresholding):
    row, column, channel = img.shape
    list1 = [255]
    list2 = [0]
    for i in range(row):
        for j in range(column):
            if img[i,j,0] >= thresholding:
                list1.append(img[i,j,0])
            else:
                list2.append(img[i,j,0])
    list1.sort() # white
    list2.sort() # black
    sum1 = sum2 = 0
    for m in range(len(list1)):
        sum1 = sum1 + list1[m]
    for n in range(len(list2)):
        sum2 = sum2 + list2[n]
    avg1 = sum1/len(list1)
    avg2 = sum2/len(list2)
    newt = int((avg1+avg2) * 0.5)
    if abs(newt - thresholding) <= 1:
        return newt
    else:
        return calculateT(img,newt)


def binary_iterative(img):
    row, column, channel = img.shape
    thresholding = random.randint(0,255)
    newt = calculateT(img, thresholding)
    binary_thresholding(img, newt)


def labelComponents(img):
    row, column, channel = img.shape
    Matrix = [[0 for x in range(column)] for y in range(row)]
    for i in range(row):
        for j in range(column):
            if img[i,j,0] == 255:
                Matrix[i][j] = 1
            else:
                Matrix[i][j] = 0

    label = 1
    list = [0,1]
    for m in range(row):
        for n in range(column):
            if Matrix[m][n] == 1:
                if Matrix[m-1][n] == 0 and Matrix[m][n-1] == 0:
                    label += 1
                    list.append(label)
                    Matrix[m][n] = label
                elif Matrix[m-1][n] != 0 and Matrix[m][n-1] == 0:
                    Matrix[m][n] = Matrix[m-1][n]
                elif Matrix[m-1][n] == 0 and Matrix[m][n-1] != 0:
                    Matrix[m][n] = Matrix[m][n-1]
                else:
                    if Matrix[m-1][n] == Matrix[m][n-1]:
                        Matrix[m][n] = Matrix[m][n-1]
                    elif Matrix[m-1][n] > Matrix[m][n-1]:
                        Matrix[m][n] = Matrix[m][n-1]
                        list[Matrix[m-1][n]] = Matrix[m][n-1]
                    else:
                        Matrix[m][n] = Matrix[m-1][n]
                        list[Matrix[m][n-1]] = Matrix[m-1][n]

    union(list)

    b = set(list)
    b1 = [k for k in b]
    numsofColor = len(b1)


    arr = []
    for x in range(numsofColor):
        count = random.randint(1,7)
        if count == 1:
            x = random.randint(30,255)
            arr.append([x,0,0])
        elif count == 2:
            x = random.randint(30,255)
            arr.append([0,x,0])
        elif count == 3:
            x = random.randint(30,255)
            arr.append([0,0,x])
        elif count == 4:
            x = random.randint(30,255)
            arr.append([x,x,0])
        elif count == 5:
            x = random.randint(30,255)
            arr.append([x,0,x])
        elif count == 6:
            x = random.randint(30,255)
            arr.append([0,x,x])
        else:
            x = random.randint(30,255)
            arr.append([x,x,x])

  # arr = types of color
  # b1 = types of labels

    for i in range(row):
        for j in range(column):
            for k in range(1,len(b1)):
                if list[Matrix[i][j]] == b1[k]:
                    img[i][j] = arr[k]
    return img


def find(i,list):
    if (i != list[i]):
        list[i] = find(list[i],list)
    return list[i]


def union(list):
    i = len(list)-1
    while i != 1:
        find(i,list)
        i  = i - 1
    return list


def histogram(img):
    row,column,channel = img.shape

    list1 = []
    list2 = []

    for i in range(256):
        list1.append(0)

    for i in range(256):
        list2.append(i)

    for i in range(row):
        for j in range(column):
            list1.append(img[i][j][0])

    list1 = list1[:-1]
    plt.hist(list1, bins=list2)
    plt.show()



#np.set_printoptions(threshold=np.inf)
img = mpimg.imread('sample.jpeg')
#plt.imshow(img, interpolation='nearest')
img.flags.writeable = True

# rgbToGray(img)
# smooth_avg(img)
# salt_pepper(img)
# smooth_median(img)
# binary_thresholding(img,180)
# binary_ptile(img,35)
#binary_iterative(img)
#smooth_median(img)
#smooth_median(img)
# smooth_median(img)
# smooth_median(img)
# histogram(img)



#labelComponents(img)

plt.imshow(img)
#plt.savefig('sample4.png')
plt.show()

