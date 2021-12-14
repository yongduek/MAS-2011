#!/usr/bin/env python

import cv2
import numpy as np

def draw_corners(img, pts):
    colors = [ (0,0,255), (0, 255, 0), (255, 0, 0), (255, 255, 100)]
    for i, xy in enumerate(pts):
        print(xy, xy.shape, xy.dtype)
        img = cv2.circle(img, xy.astype(int), radius=5, color=colors[i%4], thickness=3)
    return img

if __name__ == '__main__' :

    # Read source image.
    im_src = cv2.imread('book2_1.png')
    # Four corners of the book in source image
    pts_src = np.array([[141, 131], [480, 159], [493, 630],[64, 601]], dtype=float)

    im_src = draw_corners(im_src, pts_src)
    
    # Read destination image.
    im_dst = cv2.imread('book1.jpg')
    # Four corners of the book in destination image.
    pts_dst = np.array([[318, 256],[534, 372],[316, 670],[73, 473]], dtype=float)

    im_dst = draw_corners(im_dst, pts_dst)

    # Calculate Homography
    h, status = cv2.findHomography(pts_src, pts_dst)
    
    # Warp source image to destination based on homography
    im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1],im_dst.shape[0]))
    
    im_sum = cv2.addWeighted(im_dst, 0.5, im_out, 0.5, gamma=0)

    # Display images
    cv2.imshow("Source Image", im_src)
    cv2.imshow("Destination Image", im_dst)
    cv2.imshow("Warped Source Image", im_out)
    cv2.imshow("Sum of two", im_sum)

    cv2.waitKey(0)
