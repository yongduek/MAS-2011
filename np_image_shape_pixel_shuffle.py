import cv2, numpy as np 

def deg2rad(deg):
    return deg * np.pi / 180

def main():
    src = cv2.imread("pixels/image-15.png")
    shape = src.shape
    
    while True:
        cv2.imshow("src", src)
        
        im = src.copy().reshape((-1,3))
        n = im.shape[0]
        print(f"Pixels: {n}")
        p = np.random.permutation(n) # returns a suffled version of [0 .. n-1]
        im = im[p]
        im = im.reshape(shape)
        #
        cv2.imshow("permuted", im)
        
        # random shuffle along row direction
        im = src.copy()
        for r in range(im.shape[0]):
            row = im[r]
            row = row[ np.random.permutation(row.shape[0]) ]
            im[r] = row 
        cv2.imshow("row shuffle", im)
        
        im = src.copy()
        for c in range(im.shape[1]):
            im[:,c,:] = im[:,c,:][np.random.permutation(im.shape[0])]
        cv2.imshow("col shuffle", im)
        
        ch = cv2.waitKey(100)
        if ch == 27: break 
    #


if __name__ == "__main__":
    
    im = np.random.randint(low=0, high=256, size=(2,3,3), dtype='uint8')
    print(im) 
    shape = im.shape 
    im = im.reshape((-1,3)) # a long column of 3-vectors
    print(im)
    print('---', '\n', im.reshape(shape))  # back to original shape
    print("---\n", im.reshape((-1,3))[np.random.permutation(6)].reshape(shape))
    
    main()
