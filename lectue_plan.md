# 1. Intro to image/video data
## 1.1 Course logistics
## 1.2. image data structure, creation, indexing, visualization
1. install `pip install opencv-python`
2. install `vscode` 
3. open and display an image: `image_display.py`
   1. basic python functions to deal with command line interface
   2. opencv for reading image
   3. numpy array shape
   4. vscode debuger interface
      1. check 'dtype', 'shape', 'size'
4. change pixel values in the code: `image_change_pixels.py`
   1. BGR in opencv's image representation
   2. image pixel range: [0, 255] `dtype=uint8`. What is this?  `image_uint8.py`
5. create an image data and display: `image_create.py`
   1. manipulating the shape of a numpy array
   
## 1.3 2D drawing by cv2 functions
0. basic drawing: `cv2_drawings.py`
1. cv2 drawing functions: https://docs.opencv.org/4.6.0/d6/d6e/group__imgproc__draw.html 
   1. `cv2.line()`
   2. `cv2.putText()`
   3. `cv2.rectangle()`
   4. `cv2.fillPoly()`
   5. `cv2.ellipse()`
   6. `cv2.arrowedLine()`
   7. `cv2.circle()`
   8. `cv2.drawMarker()`
2. **Assignment** 
    - Use every drawing function above. Choose one at random, draw a figure with random parameters.


# 2. Algorithmic drawing and visualization
## Iterated Function System (IFS)
1. Hill's book pp. 69-73

## 2.1 Sierpinski triangle
- https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle 
1. Algorithm:
   1. Choose three fixed points T0, T1, T2
   2. Choose the initial point p0 to be drawin by selecting one of the points T0, T1, T2
   3. Repeat
      1. Choose one of the three points at random; call it T
      2. Construct the next point $p_k$ as the midpoint between T and $p_{k-1}$
      3. Draw a dt at $p_k$ 
2. code: `ifs_sierpinski_gasket.py`

## 2.2 Clifford Attractors
- source: https://examples.pyviz.org/attractors/attractors.html 
- An attractor is a set of values to which a numerical system tends to evolve. It is called a strange attractor if the resulting pattern has a fractal structure.
1. Algorithm: 
$$
x_{n +1} = \sin(a y_{n}) + c \cos(a x_{n})\\
y_{n +1} = \sin(b x_{n}) + d \cos(b y_{n})
$$
2. code: `ifs_clifford_attractor.py`
   ```
        # init & parameters               
        x, y, a, b, c, d = 0, 0, -1.3, -1.3, -1.8, -1.9
    ```
3. Notice the role of `scale` and `shift`.

## 2.3 Gumowski-Mira Attractor 
1. Algorithm
    ```
    def f(x):
        return a * x + 2.0 * (1.0 - a) * x * x / (1.0 + x * x)

    def gm(x, y):
        xnew = b * y + f(x)
        y = -x + f(xnew)       # update
        x = xnew               # update
        return (x, y)

    (x, y) = gm(x, y)
    ```
2. code: `ifs_Gumowski_Mira_attractor.py`


## 2.4 DIY Project
0. Finish 'Project 1: Plotting the Hailstone Sequence' in Hill's p.71.
1. Produce a view of the attractor of your choice.
2. Produce a video: https://github.com/vdesmond/attractors

## 2.5 More?
1. https://softologyblog.wordpress.com/ 


---
# 3. Viewport Transformation
Graphs are drawn in their generic domain. E.g. $y = sin(x)/x$ defined for $x \in [-2\pi, 2\pi]$ will be ranged in $[-1, 1]$. After obtaining the graph pairs $\{(x_i, y_i)\}$, the coordinates are scaled and shifted to the window coorddinate system; this is called the viewport transformation.

## 3.1 Procedure (drawing a graph)
1. obtain a set of points $\{(x_i, y_i)\}$ with an appropriate x grid.
2. define your own window rectangle in the world: left, right, bottom, top.
    - e.g. left=$-2\pi$, right = $+2\pi$, bottom = -1.2, top = +1.2
3. define your window rectangle in the display pixel window.
    - e.g. $d.lrbt = [50, 550, 600, 20]$ where $y$ coordinate is reversed.
4. compute the viewport transformation: $T: w \rightarrow d$
$$
    \frac{x_w - w.l}{w.r - w.l} = \frac{x_d - d.l}{d.r - d.l}
$$
$$
    x_d = \frac{x_w - w.l}{w.r - w.l} \times (d.r - d.l) + d.l
$$

5. put pixels or draw lines.

**DIY**: Try to draw a graph in two parallel viewport windows, which will give you two views of the same graph.

## 3.2 `numpy` array
- https://buildmedia.readthedocs.org/media/pdf/howtothink/latest/howtothink.pdf 

---
# 4. Parametric curves
## 4.1 Regular polygons, ellipses, circles
$$
    x = r \cos\theta \\
    y = r \sin\theta
$$

## 4.2 Polysprials (with turtle graphics)

## 4.3 Polar coordinate shapes
$$
    p = r e^{i\theta} \in \mathbb{R}^2 \\
$$
$$
    r(\theta) = f(\theta)
$$


# 5. DIY Line Drawing

`np_line_drawing.py`

## 5.1 Simple line drawing

## 5.2 Triangles and filled triangles

- How to sort by row and then column

## 5.3 The Bresenham algorithm (DIY Team Project)
- Will be presented.

# 6. Rotation and Translation
## 6.1 Coordinate representation
- Change of basis
- Meaning of rotation matrix

## 6.2 Linear interpolation in 1D
- https://en.wikipedia.org/wiki/Linear_interpolation 
- Expanding two samples to three, four or five.
- Three ways of grid aligning 
    1. `align_corners = T/F`  in `pytorch.nn.functinoal.interpolate()` 
    2. align so that source pixels are not modified in the destination; the last pixels will become just copies of the last source pixel (which is also an option)

# 7. 2D Affine Transformation
- Shear, scaling in addition to rotation and translation
- parallelis is invariant.

## 7.1 Triangle transformation
- Sequential formulation of 2D affine transformations from one triangle to another
- Or by linear algebra
## 7.2 Homogeneous coordinate representation
- Matrix multiplications to obtain the sequential transformations.


# 8. Intermission


# 9. Pixel-based Image Processing
- Binary images
- Bit planes of a gray scale image
- Color representation: RGB & HSV
- Color negation
- Pixel-swap: random swap; brightness sorting in column

## DIY Project: Chorma-keying or Digital Matting

# 10. Histogram
- How to compute histogram in 1D, 2D, and 3D
- Brightness & contrast control by histogram transformation
- Gamma correction
- Histogram equalization algorithm

# 11 Convolution - Mask Operation
- Linear algebra: dot product or inner product
- Smoothing of 1D signal
    - box kernel; Gaussian kernel
- Gradient with DOG 
- LOG and zero-crossing for edge finding
- Convolution vs correlation
    - Convolution with DOG, LOG for a 1D step edge signal
- 2D Masking for image blurring
- Spatial gradient: Sobel operator, mag & direction
- Canny edge detector
- Gabor filter & Fractalius effect
- 
# 12 Morphological Operation
- Structuring element to choose operation window
- Min & Max operation
- Dilation & erosion
- Closing & opening
# 13. 2D Projective Transformation
- 2D Perspective transformation and pin-hole camera effect
- $3\times3$ Homography matrix
- Planar transformation in 3D perspective

## DIY Project: Stitching two images having a common planar view

# 14. Coding, Compression, and Harmonic Analysis
- Linear algebra revisited: orthonormal basis & change of basis
- PCA
- SVD
- DFT

# 15. Further Readings