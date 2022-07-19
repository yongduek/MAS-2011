# MAS-2011
Materials for MAS-2011

## Preliminaries
1. C/C++ will be mainly used. Students are expected to install necessary packages.
    - Visual Studio for MS Windows 10/11
    - XCode for Mac OS X
2. OpenCV will be utilized.
    - Install opencv library.
    - www.opencv.org 
    

Video Files
- production_ID_5155396.mp4: Video by Dmitry Varennikov from Pexels (https://www.pexels.com/video/time-lapse-video-of-star-gazing-on-a-starry-night-5155396/)

## 0. Drawing
1. dot
1. line, random lines
1. triangle
1. polygon
    - regular polygons, connecting adjacent vertices
    - stellation (starlike) figure, connecting every other vertex
    - rosette figure, connecting each vertex to every other vertex
3. circle
4. ellipse
    - $((x-x0)/W)^2 + ((y-y0)/H)^2 = 1$
5. Polar coordinate shapes
    - $x(t) = r(t) cos(\theta(t))$
    - $y(t) = r(t) sin(\theta(t))$
    - $r(t) = K(1+\cos(\theta))$ : Cardioid
    - $r(t) = K \cos(n\theta)$ : Rose curves, where $n$ specifies the number of petals in the rose.
7. moving polygons: affine transformation & kinematics
8. draw a robot hand of two joints
9. draw a 2D planet system

## 1. Movie Barcode
1. open a movie file
    1. read a frame
    1. do calculation on the frame
    1. accumulate the result
    1. resize the final result
1. save to an image file '.png'

## 2. Geometric Transformation
1. rotate an image `rotate_image.py`
1. online rotation of an image to make a movie `rotate_image_motion.py`
1. Affine transformation
    - rotation, translation, scaling, homogeneous vector representation
    - order of transformation
    - `rotate_image_motion_diy.py`
        1. `numpy` for vector/matrix computation

## 3. Linear & Bilinear Interpolation
1. linear interpolation: $f(t) = a + bt$ for $t\in[0,1]$
    - wikipedia
1. bilinear interpolation
1. forward/backward transformation
1. DIY geometric transformation, revisited.
1. principle of texture mapping: affine transformation between two triangles
1. 2D perspective (projective) transformation
    1. rectification
    1. stitching images

## 4. Coding, Compression and Fourier Analysis
1. Orthogonal basis (linear algebra) & representation of a frame of data
    1. Orthogonal == zero inner product, linear algebra revisted
1. Fourier basis in complex numbers
1. DFT, DCT, FFT
1. SVD as a compressor with minimum L2 reconstruction error

## 5. Pixel Operation
- pixel_operations.ipynb
1. bitplanes of gray scale image
1. color rotation
    - RGB is a selection of three light spectrums
    - HSV/HSL/YUV/Lab to represent color information
1. Negation in RGB and HSV

## 6. Histogram operation
1. brightness vs contrast
1. image-level control of brightness and contrast
1. gamma control
1. linear constrast expansion
1. nonlinear histogram equalization 

## 7. Window Operation: Convolution or Correlation
1. Smoothing of 1D: moving average of an audio wave or a single column of an image
    - inner product again
    - shape change and border manipulation
1. box blurring
1. Gaussian smoothing/blurring
1. Spatial gradient: Sobel or DoG
    - Gradient: magnitude and direction in 2D, revisited
1. Canny edge detector to get binary edge map
1. Local feature detector: Gabor filter, DoG, LoG
1. Supervised learning for feature detection (canny, sobel)
1. Supervised learning for high-level classification (cat-dog, hand written digits)


---
## Pygame
- learning by doing

### Pygame Resources
1. [game development with Pygame by kidscancode.org](https://www.youtube.com/playlist?list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw)
1. [sprite sheet tutorial: load, parse, and use](https://youtu.be/ePiMYe7JpJo)


---
## Reinfocement Learning
1. RLBook by Sutton
