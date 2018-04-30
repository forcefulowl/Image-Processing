- Computer graphic: the process of creating images from abstract model. For e.g. there's a list/Matrix of points, each point correspond to each pixel of the image.<br>
- Image processing: Starting with an exsiting image and using different methods to refine it.

Gray-Scale Image:<br>
for e.g. RGB image (3 channels), if n bits/cell or n bits/pixel, which means n/3 bits per channel, as the result the image can show `math.pow(2,n)` types of color, and `math.pow(2,n/3)` types of shades of gray

CLT (color look-up table): Increase the nums of option of color<br>
for e.g. 9 bits for each cell/pixel, so there can be `math.pow(2,9)` types of color in the image, but if the size of each row of CLT is `math.pow(2,12)`, then the option of color is `math.pow(2,12)`

Image histogram and info content

Linear contrast enhancement method and its implementation:<br>
If the image suffers from low-contrast, we can use contrast enhancement, but we will miss info of the image.

Conversion of color to gray-scale:<br>

luminosity:

```python
            avglist = img[i,j]
            
            avg = int(avglist[0]*0.299 + avglist[1]*0.587 + avglist[2]*0.114)
            
            img[i,j] = [avg,avg,avg]
```
***
### Conversion of gray-scale to B&W:<br>
0. Slicing: When multiple peeks appears in a histogram, use multiple t, compute each of them then combine the results.
1. Simple thresholding: `img[i,j,0] > t -> White, else -> Black`<br>
2. P-Tile: Top x% pixel be white, others be black<br>
3. Iterative threshold selection: <br>

```
t = random.randint(0,255)
using t as thresholding to convert the image to B&W
compuing the avg value of each part a1,a2
newt = (a1+a2)/2
if abs(newt-t) < 1:
	return newt
else:
	using t as thresholding to convert the image to B&W and computing a1,a2 until (newt-t)<1

```

***

#### Low-pass filter:<br>

- All values in masks are positive

- The sum of all the values equals to 1

- The boundary content is reduced by using a low-pass filter

- As the size of mask grows, more smoothing will take place

#### High-pass filter:<br>

- A mask have positive and negative values

- The sum of all values in a mask is equal to 0

- The boundary content is increased by a high-pass mask

- As the size of mask grows, more boundary content is increased

***

### Noise Reduction:<br>

- averaging: NS5

- Median: NS9

Smoothing using thresholding: withour lossing boundary.

***

Component labeling and applications:

***
### Image sharpening:<br>

0. gradient operators<br>

1. 1st and 2nd order derivatives: 1st order: gradient operators; 2nd order: Laplacian operator<br>

2. Robert's operator: `[0,-1,1,0]+[-1,0,0,1]`<br>
3. sharpening by thresholding: base on Robert's<br>
4. Laplacian operator<br>
`ori1 = [0,1,0,1,-4,1,0,1,0], ori2 = [1,0,1,0,-4,0,1,0,1], new = [1,1,1,1,-8,1,1,1,1]`<br>
5. Prewitt operator: child<br>
`r1 = [-1,0,1,-1,0,1,-1,0,1], r2 = [1,1,1,0,0,0,-1,-1,-1], result = math.sqrt(r1**2+r2**2)`<br>
6. Kirsh operator: parent<br>
`r3 = [0,1,1,-1,0,1,-1,-1,0], r4 = [1,1,0,1,0,-1,0,-1,-1], result = max(r1,r2,r3,r4)`<br>
7. Sobel operator:<br>
 `x = [1,2,1,0,0,0,-1,-2,-1], y = [1,0,-1,2,0,-2,1,0,-1], result = math.sqrt(x**2+y**2)`<br>
8. conversion of high-pass filtered images into B&W
***

### Parallel Processing & HPC

- ALU: Arithmetic Logic Unit<br>
- MCU: Master Control Unit<br>

####Grosch's Law <br>
To sell a computer for twice as much, it must be four times faster.<br>

#### Von Neumann's Design Rule <br>

Multiple Processors performance = N\*T - V <br>
 - N: No. of processors <br>
 - T: No. of Instructions per second for each <br>
 - V: Communication Overhead <br>

#### Amdahl's Law <br>
 
 `Speedup = T(1) / T(N)` <br>
 Speedup is the theoretical speedup of the execution of the whole task. <br>
 - B: The serial part of the code can be computed in the equal to `BT(1)` <br>
 - (1-B): The parellel part of the code can be computed in the equal to `(1-B)T(1) / N` <br>
 `Speedup = T(1) / (T(1)B + T(1)(1-B)/N) = N / (BN + (1-B))`  <-- Pessimistic View <br>

 Eg. Assume N = 10, B = 0.67, (1-B) = 0.33 <br>
 ==> `Speedup = 1/(0.67+(0.33/10)) = 1.42` <-- This is not ideal<br>
#### Gustafson's Law <br>
 Consider B & N are not independent
 `Speedup = T(1)/T(N)`<br>
 If N = 1, `T(1) = B + (1-B)N`<br>
 If N > 1, `T(N) = B + (1-B) = 1` <br>
 `Speedup = [B + (1-B)N]/1`,  `Speedup = N - B(N-1) or N + B(1-N)`  <-- Optimistic View<br>
 Eg. Assume N = 10, B = 0.67, (1-B) = 0.33 <br>
 ==> `Speedup = 10 - 0.67(9) = 3.97 ~= 4` <-- Expected the speedup of 4.<br>
