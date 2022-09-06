import os, sys 
import numpy as np 
import cv2 

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) == 1:
        imagefile = "pixels/cow.jpg"
    else:
        imagefile = sys.argv[1]
    print(f"Image: {imagefile}")
    
    if os.path.exists(imagefile) == False:
        print(f"File does not exist: {imagefile}")
        sys.exit(1)
    
    im = cv2.imread(imagefile)
    
    # make another array
    im2 = im.copy() # hard copy 
    
    # change color
    im2[100:200, 100:400] = [255, 0, 0]  # BGR
    
    
    while True:
        cv2.imshow("dispWindow", im)
        # another window
        cv2.imshow("dispWindow2", im2)
        
        ch = cv2.waitKey(10)  # press ESC to stop
        if ch == 27: break