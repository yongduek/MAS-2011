# MAS-2011
Materials for MAS-2011


Video Files
- production_ID_5155396.mp4: Video by Dmitry Varennikov from Pexels (https://www.pexels.com/video/time-lapse-video-of-star-gazing-on-a-starry-night-5155396/)

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
1. DIY image rotation, revisited.
