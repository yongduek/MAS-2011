# 1. Intro to image/video data
## 1.1 course logistics
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

## 2.1 Sierpinski gasket
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


## 2.4 Try
0. Finish 'Project 1: Plotting the Hailstone Sequence' in Hill's p.71.
1. Produce a view of the attractor of your choice.
2. Produce a video: https://github.com/vdesmond/attractors

## 2.5 More?
1. https://softologyblog.wordpress.com/ 