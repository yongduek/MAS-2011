import os, sys 
import numpy as np 
import cv2 

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) == 1:
        imagefile = "pixels/월인석보_세종어제훈민정음부월인석보.jpeg"
    else:
        imagefile = sys.argv[1]
    print(f"Image: {imagefile}")
    
    if os.path.exists(imagefile) == False:
        print(f"File does not exist: {imagefile}")
        sys.exit(1)
    
    im = cv2.imread(imagefile)
    
    while True:
        cv2.imshow("dispWindow", im)
        
        ch = cv2.waitKey(10)  # press ESC to stop
        if ch == 27: break