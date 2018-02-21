# Image-Processing

The original image used in this project is:

![avatar](/img/original.png)

### Add Noise

Using Salt-pepper, randomly changing the value of pixels to [0,0,0] or [255,255,255].

![avatar](/img/salt-pepper.png)


### Noise Reduction
***Average Smooth***

Using NS5 to caculate the average value.

***Median Smooth***

Using NS9 to caculate the median value. Now using *Median Smooth* on the noised version.

![avatar](/img/median-filter.png)

### Gray-Scale to Binary

The most common way is to set a thresholding, if the value of pixel is larger than that thresholding, setting the value of pixel as [255,255,255], if not, setting it as [0,0,0].

There're two more methods which can achieve the goal, the first one is *P-Tile*, which means the pixel with the top x% value can be converted to white, others should be converted to black.

And the second one is *Iterative Thresholding*. 
- Setting T as a random number, and appling the T to the common thresholding method. 
- Caculating the new thrsholding T' = 1/2(a1+a2).<br>a1 = the average of the value of pixel which is larger than T, <br>a2 = the average of the value of pixel which is smaller than T, and caculating the absolute value of (T-T'). 
- If the result is larger than 1 (whatever), using T' as T to continue the above loop, until the result is smaller than 1, finally, the T' in last loop should be the thresholding in converting.

![avatar](/img/iterative-binary.png)

### Label-Component

The main purpose of *Label-Component* is to detect the number of components the image has. It can be only applied to binary images. The initial value/label of the image is: the label of white part is 1, the label of black part (usually background)
is 0, we usually say the pixel with label 0 is invalid, and when scaning the whole image, there're three conditions should be followed, for e.g., when scaning img[i][j]:
- if the label of top and left pixel are invalid, the label of img[i][j] = label ++
- if one of the label of top and left pixel is invalid, the label of img[i][j] = the label of the valid one.
- if both the label of top and left pixel are valid,<br>If the label of top = the label of left, the label of img[i][j] = that label.<br>If the label of top and left pixel is different, the label of img[i][j] = the smaller one.


