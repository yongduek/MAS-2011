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
