# MAS-2011
Materials for MAS-2011

## * Preliminaries
1. C/C++  and/or Python will be mainly used. Students are expected to install necessary packages.
    - https://code.visualstudio.com/docs/languages/cpp 
      - with MinGW64
    - XCode for Mac OS X for C/C++ Programming
    - Python3 with VSCode.
    - Visual Studio Community 2019 for MS Windows 10/11 - Install C/C++
  
2. OpenCV library will be utilized a lot!.
    - Install opencv library.
    - www.opencv.org 

3. Install Opencv 3.x
   1. C/C++: 
     - install: `cmake`, `cmake-gui`, and then download opencv source code to install.
     - we will be installing opencv 3.4.x
     - https://docs.opencv.org/4.x/df/d65/tutorial_table_of_content_introduction.html 
     - Windows: https://docs.opencv.org/4.x/d3/d52/tutorial_windows_install.html 
       - Installation in Windows may be more tricky than in Mac OS X or Linux; but the same procedure using `camke` or `cmake-gui`
   2. Python3: `pip install opencv-python`
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
1. [Kidscancode.org: Game development with Pygame](https://www.youtube.com/playlist?list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw)
1. [sprite sheet tutorial: load, parse, and use](https://youtu.be/ePiMYe7JpJo)
1. [Programming Arcade Games with Python and Pygame](http://programarcadegames.com/)
2. [Arcade Academy - Learn Python](https://learn.arcade.academy/en/latest/)
    1. [The Python Arcade Library](https://api.arcade.academy/en/latest/)
    4. [Tutorial: Build a platform game in python with arcade (realpython.com)](https://realpython.com/platformer-python-arcade/#:~:text=Install%20the%20Python%20arcade%20library%20Create%20a%20basic,joystick%20input%20Play%20sound%20effects%20for%20game%20actions)
        1. concise and good.
        2. a list of resources and apps for pygame and arcade.

---
## Reinfocement Learning
1. RLBook by Sutton


## Install MinGW64 & OpenCV in Windows.
* This is partly from https://code.visualstudio.com/docs/languages/cpp 
1. MinGW64: https://www.msys2.org/ 
   1. Go here, follow all the commands to install mingw-w64 including `gcc`, `g++` etc.
      1. In the `MSYS2 MSIS` terminal:
         1. `/bin/pacman -Syu` might be useful instead of `pacman -Syu`
   2. if MSYS is installed in C drive, then you will see `c:/msys64`
      1. run `mingw64` in the directory for c/c++ development.
      2. this terminal will be mainly used for installations.
   3. Add the MinGW compiler to your PATH: https://code.visualstudio.com/docs/languages/cpp
        * Add the path to your Mingw-w64 bin folder to the Windows PATH environment variable by using the following steps:

          1. In the Windows search bar, type 'settings' to open your Windows Settings.
          2. Search for Edit environment variables for your account.
          3. Choose the Path variable in your User variables and then select Edit.
          4. Select New and add the Mingw-w64 destination folder path, with \mingw64\bin appended, to the system path. The exact path depends 5. on which version of Mingw-w64 you have installed and where you installed it. If you used the settings above to install Mingw-w64, then add this to the path: C:\msys64\mingw64\bin.
          5. Select OK to save the updated PATH. You will need to reopen any console windows for the new PATH location to be available.
          Check your MinGW install


2. https://cmake.org/ 
3. https://gitforwindows.org/ 
4. open `git-bash`, a command line tool included in the `git` package.
5. download opencv
    ```
    $ mkdir https://github.com/opencv/opencv.git`
6. install it.
