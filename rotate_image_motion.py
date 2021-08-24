# https://learnopencv.com/image-rotation-and-translation-using-opencv/

import cv2

image = cv2.imread('pixels/image-15.png')
# dividing height and width by 2 to get the center of the image
height, width = image.shape[:2]
# get the center coordinates of the image to create the 2D rotation matrix
center = (width/2, height/2)

degree, da = 0, 5
while cv2.waitKey(30) != 27:
    # using cv2.getRotationMatrix2D() to get the rotation matrix
    rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=degree, scale=.707)  # the object rotates -45 actually
    print(image.shape, center, rotate_matrix)

    # rotate the image using cv2.warpAffine
    rotated_image = cv2.warpAffine(src=image, M=rotate_matrix, dsize=(width, height))
    # cv2.imshow('Original image', image)

    cv2.putText(rotated_image, f'{degree:3d}', (0, height), 
                fontFace=cv2.FONT_HERSHEY_PLAIN,
                fontScale=1.8,
                color=(250, 255, 10))

    cv2.imshow('Rotated image', rotated_image)

    degree = (degree + da) % 360
# end.