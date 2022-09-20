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
    s = im.shape
    print(s)
    # cv2.imshow("window", im)

    # cv2.waitKey(0)

    while True:
        x = np.random.randint(0, s[1]-10)
        y = np.random.randint(0, s[0]-10)

        color = np.random.randint(0, 256, size=3)
        # print(color)

        im[y:y+10, x:x+10] = color 

        # im[y:y+10, x:x+10, 0] = color[0] 
        # im[y:y+10, x:x+10, 1] = color[1]
        # im[y:y+10, x:x+10, 2] = color[2]

        cv2.imshow("dispWindow", im)
        
        ch = cv2.waitKey(1)  # press ESC to stop
        if ch == 27: break



#