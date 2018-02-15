import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from copy import deepcopy
import math
import random

class test():
    def __init__(self,row,column,channel):
        self.row = row
        self.column = column
        self.channel = channel


    def salt_pepper(self,img):
        row, column, channel = img.shape
        nums = int((row * column) * 0.1)
        for i in range(nums):
            num1 = random.randint(0, row - 1)
            num2 = random.randint(0, column - 1)
            if img[num1, num2, 0] >= 100:
                img[num1, num2] = [0, 0, 0]
            else:
                img[num1, num2] = [255, 255, 255]
        return img

    def smooth_avg(self,img):
        row, column, channel = img.shape
        img1 = deepcopy(img)
        for i in range(1, row - 1):
            for j in range(1, column - 1):
                img[i, j, 0] = math.floor(img1[i, j, 0] * 0.2) + math.floor(img1[i - 1, j, 0] * 0.2) + math.floor(
                    img1[i, j - 1, 0] * 0.2) + math.floor(img1[i, j + 1, 0] * 0.2) + math.floor(img1[i + 1, j, 0] * 0.2)
                # img[i,j,1] = math.floor(img1[i,j,1]*0.2)+math.floor(img1[i-1,j,1]*0.2)+math.floor(img1[i,j-1,1]*0.2)+math.floor(img1[i,j+1,1]*0.2)+math.floor(img1[i+1,j,1]*0.2)
                # img[i,j,2] = math.floor(img1[i,j,2]*0.2)+math.floor(img1[i-1,j,2]*0.2)+math.floor(img1[i,j-1,2]*0.2)+math.floor(img1[i,j+1,2]*0.2)+math.floor(img1[i+1,j,2]*0.2)
                img[i, j, 1] = img[i, j, 2] = img[i, j, 0]
        return img

    def smooth_median(self,img):
        row, column, channel = img.shape
        img1 = deepcopy(img)
        for i in range(1, row - 1):
            for j in range(1, column - 1):
                list = [img1[i - 1, j - 1, 0], img1[i - 1, j, 0], img1[i - 1, j + 1, 0], img1[i, j - 1, 0],
                        img1[i, j, 0], img1[i, j + 1, 0], img1[i + 1, j - 1, 0], img1[i + 1, j, 0],
                        img1[i + 1, j + 1, 0]]
                list.sort()
                img[i, j, 0] = img[i, j, 1] = img[i, j, 2] = list[4]
        return img

    def binary_thresholding(self, img):
        row, column, channel = img.shape
        for i in range(row):
            for j in range(column):
                if img[i, j, 0] >= 180:
                    img[i, j] = [255, 255, 255]
                else:
                    img[i, j] = [0, 0, 0]
        return img

    def binary_ptile(self, img):
        row, column, channel = img.shape
        nums = row * column
        list = []
        for i in range(row):
            for j in range(column):
                list.append(img[i, j, 0])
        list.sort()
        p = list[int((nums - 1) * (1 - 35 * 0.01))]
        for i in range(row):
            for j in range(column):
                if img[i, j, 0] >= p:
                    img[i, j] = [255, 255, 255]
                else:
                    img[i, j] = [0, 0, 0]
        return img

    def calculateT(self, img, thresholding):
        row, column, channel = img.shape
        list1 = [255]
        list2 = [0]
        for i in range(row):
            for j in range(column):
                if img[i, j, 0] >= thresholding:
                    list1.append(img[i, j, 0])
                else:
                    list2.append(img[i, j, 0])
        list1.sort()  # white
        list2.sort()  # black
        sum1 = sum2 = 0
        for m in range(len(list1)):
            sum1 = sum1 + list1[m]
        for n in range(len(list2)):
            sum2 = sum2 + list2[n]
        avg1 = sum1 / len(list1)
        avg2 = sum2 / len(list2)
        newt = int((avg1 + avg2) * 0.5)
        if abs(newt - thresholding) <= 1:
            return newt
        else:
            return self.calculateT(img, newt)

    def binary_iterative(self, img):
        row, column, channel = img.shape
        thresholding = random.randint(0, 255)
        newt = self.calculateT(img, thresholding)
        for i in range(row):
            for j in range(column):
                if img[i,j,0] >= newt:
                    img[i,j] = [255,255,255]
                else:
                    img[i,j] = [0,0,0]
        return img


    def labelComponents(self,img):
        row, column, channel = img.shape
        Matrix = [[0 for x in range(column)] for y in range(row)]
        for i in range(row):
            for j in range(column):
                if img[i, j, 0] == 255:
                    Matrix[i][j] = 1
                else:
                    Matrix[i][j] = 0

        label = 1
        list = [0, 1]
        for m in range(row):
            for n in range(column):
                if Matrix[m][n] == 1:
                    if Matrix[m - 1][n] == 0 and Matrix[m][n - 1] == 0:
                        label += 1
                        list.append(label)
                        Matrix[m][n] = label
                    elif Matrix[m - 1][n] != 0 and Matrix[m][n - 1] == 0:
                        Matrix[m][n] = Matrix[m - 1][n]
                    elif Matrix[m - 1][n] == 0 and Matrix[m][n - 1] != 0:
                        Matrix[m][n] = Matrix[m][n - 1]
                    else:
                        if Matrix[m - 1][n] == Matrix[m][n - 1]:
                            Matrix[m][n] = Matrix[m][n - 1]
                        elif Matrix[m - 1][n] > Matrix[m][n - 1]:
                            Matrix[m][n] = Matrix[m][n - 1]
                            list[Matrix[m - 1][n]] = Matrix[m][n - 1]
                        else:
                            Matrix[m][n] = Matrix[m - 1][n]
                            list[Matrix[m][n - 1]] = Matrix[m - 1][n]

        self.union(list)

        b = set(list)
        b1 = [k for k in b]
        numsofColor = len(b1)

        arr = []
        for x in range(numsofColor):
            count = random.randint(1, 7)
            if count == 1:
                x = random.randint(30, 255)
                arr.append([x, 0, 0])
            elif count == 2:
                x = random.randint(30, 255)
                arr.append([0, x, 0])
            elif count == 3:
                x = random.randint(30, 255)
                arr.append([0, 0, x])
            elif count == 4:
                x = random.randint(30, 255)
                arr.append([x, x, 0])
            elif count == 5:
                x = random.randint(30, 255)
                arr.append([x, 0, x])
            elif count == 6:
                x = random.randint(30, 255)
                arr.append([0, x, x])
            else:
                x = random.randint(30, 255)
                arr.append([x, x, x])

        # arr = types of color
        # b1 = types of labels

        for i in range(row):
            for j in range(column):
                for k in range(1, len(b1)):
                    if list[Matrix[i][j]] == b1[k]:
                        img[i][j] = arr[k]
        return img

    def find(self,i, list):
        if (i != list[i]):
            list[i] = self.find(list[i], list)
        return list[i]

    def union(self,list):
        i = len(list) - 1
        while i != 1:
            self.find(i, list)
            i = i - 1
        return list

# img = mpimg.imread('/Users/gavin/Desktop/sample4.jpeg')
#
# img.flags.writeable = True