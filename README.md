# MAS-2011
Materials for MAS-2011

## * Preliminaries
1. C/C++ will be mainly used. Students are expected to install necessary packages.
    - Visual Studio for MS Windows 10/11 - Install C/C++
    - XCode for Mac OS X
    - python will be used selectively.
  
2. OpenCV library will be utilized.
    - Install opencv library.
    - www.opencv.org 
    
## References
- Digital Image Processing, Rafael Gonzalez and Richard Woods.
- Computer Vision: Algorithms and Applications, 2nd ed., Richard Szeliski, https://szeliski.org/Book/
- Multiple View Geometry in Computer Vision, Richard Hartley and Andrew Zisserman
- Computer Graphics Using OpenGL (2nd Ed.), Francis S. Hill 
- Mathematics for Machine Learning, Marc Peter Deisenroth, A. Aldo Faisal, and Cheng Soon Ong, https://mml-book.github.io/
  
Video Files
- production_ID_5155396.mp4: Video by Dmitry Varennikov from Pexels (https://www.pexels.com/video/time-lapse-video-of-star-gazing-on-a-starry-night-5155396/)

## Pixel Rendering & Drawing 2D Polygons
1. OpenCV processing loop
1. indexing RGB image memory
2. image file read/write
3. dots
4. line drawing / rasterization
   1. Bresenham algorithm
5. triangles
6. polygon
    - regular polygons, connecting adjacent vertices
    - stellation (starlike) figure, connecting every other vertex
    - rosette figure, connecting each vertex to every other vertex
7. circle
8. ellipse
    - $((x-x0)/W)^2 + ((y-y0)/H)^2 = 1$
9.  Polar coordinate shapes
    - $x(t) = r(t) cos(\theta(t))$
    - $y(t) = r(t) sin(\theta(t))$
    - $r(t) = K(1+\cos(\theta))$ : Cardioid
    - $r(t) = K \cos(n\theta)$ : Rose curves, where $n$ specifies the number of petals in the rose.
9. Filling convex polygons
    - triangle-based.
10. moving polygons: affine transformation & kinematics *
11. draw a robot hand of two joints *
12. draw a 2D planet system *

## Pixel Operations
- pixel_operations.ipynb
1. color quantization to make a cartoon-like image 
1. bitplanes of gray scale image
2. color space representation: RGB, HSV
   - Hue rotation
   - RGB is a selection of three light spectrums
   - HSV/HSL/YUV/Lab to represent color information
3. Negation in RGB and HSV
4. Pixel-Swap by 이주행 

## Histogram operation
1. brightness vs contrast
1. image-level control of brightness and contrast
1. gamma control
1. linear constrast expansion
1. nonlinear histogram equalization 
1. image color swapping by histograms
2. 
## Window Operation: Convolution or Correlation
1. linear algebra revised: inner product in 1D and 2D
1. Smoothing of 1D: 
    - moving average of an audio wave or a single row/column of an image
    - inner product again
    - shape change and border manipulation
2. box blurring
3. Gaussian smoothing/blurring
4. Spatial gradient: Sobel or DoG
    - Gradient: magnitude and direction in 2D, revisited
5. Canny edge detector to get binary edge map
6. Local feature detector: Gabor filter, DoG, LoG
    - Fractalius effect
      - `intro_convolution.ipynb`
7. Supervised learning for feature detection (canny, sobel)
8. Supervised learning for high-level classification (cat-dog, hand written digits)

## Movie Barcode
1. open a movie file
    1. read a frame
    1. do calculation on the frame
    1. accumulate the result
    1. resize the final result
1. save to an image file '.png'

## Chroma-Keying / Matting
   - `chroma_keying.ipynb`
   - Term Project !

## Geometric Transformation
1. linear algebra: 
    - orthogonal basis and basis change
    - rotation matrix
    - homogeneous coordinate representation
2. rotate an image `rotate_image.py`
3. online rotation of an image to make a movie `rotate_image_motion.py`
4. Affine transformation
    - rotation, translation, scaling, homogeneous vector representation
    - order of transformation
    - `rotate_image_motion_diy.py`

## Linear & Bilinear Interpolation
1. linear interpolation: $f(t) = a + bt$ for $t\in[0,1]$
    - wikipedia
1. bilinear interpolation
1. forward/backward transformation
1. DIY geometric transformation, revisited.
1. principle of texture mapping: affine transformation between two triangles
1. 2D perspective (projective) transformation
    1. rectification
    1. stitching images

## Coding, Compression and Fourier Analysis
1. linear algebra revisited:
   - Orthogonal basis (linear algebra) & representation of a data in $\mathbb{R}^n$
3. PCA: Principal Component Analysis
   - Eigen decomposition
   - data set of random samples (from a Gaussian distribution)
5. SVD as a compressor with minimum L2 reconstruction error
   - Singular value decomposition
4. DFT & Fourier basis in complex numbers
   - Discrete Fourier Transformation for 1D and 2D signal vectors.
   - DFT as compression


---
## Pygame
- learning by doing

### Pygame Resources
1. [game development with Pygame by kidscancode.org](https://www.youtube.com/playlist?list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw)
1. [sprite sheet tutorial: load, parse, and use](https://youtu.be/ePiMYe7JpJo)


---
## Reinfocement Learning
1. RLBook by Sutton
