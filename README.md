# MAS-2011
Materials for MAS-2011


Video Files
- production_ID_5155396.mp4: Video by Dmitry Varennikov from Pexels (https://www.pexels.com/video/time-lapse-video-of-star-gazing-on-a-starry-night-5155396/)

## 0. Drawing
1. dot
1. line, random lines
1. triangle
1. polygon
1. circle
1. ellipse
1. moving polygons: affine transformation & kinematics
1. draw a robot hand of two joints
1. draw a 2D planet system

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


## Pygame
- learning by doing