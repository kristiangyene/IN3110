#!/usr/bin/env python3
import numpy
import cv2
import time
import sys

#(H, W, C) heigth, width, channels

def main():
    """Main fuction to start the program. Reads the image from either the command inputfilename or 
    the default filename "beatles.jpg" and calls the blur_image method. It also saves the image to either 
    the command outputfilename or the default filename "blurred_image1.
    
    """
    if len(sys.argv) == 3:
        filename = sys.argv[1]
    else:
        print("set image to blur as 'beatles.jpg'")
        filename = "beatles.jpg"
    src = cv2.imread(filename)
    #halves the dimensions of the image
    #src = cv2.resize(src, (0, 0), fx=0.5, fy=0.5)
    h, w, c = src.shape
    copy = numpy.empty(src.shape)

    #Padding src-image to blur edges
    src = numpy.pad(src, ((1,1),(1,1),(0,0)), mode='edge')
    src = src.astype("uint32")

    #Call method that returns blurred image 
    startTime = time.time()
    dst = blur_image(src, copy, h, w, c)
    endTime = time.time()
    #writeTime(endTime-startTime, filename)

    dst = dst.astype("uint8")
  
    if len(sys.argv) == 3:
        cv2.imwrite(sys.argv[2], dst)
    else: 
        print("Saved blurred image as 'blurred_image1.jpg'\n\nTo specify input-/",
        "outputfile use: blur.py [-h] blur_program input_filename output_filename\n")
        cv2.imwrite("blurred_image1.jpg", dst)
   

#Blur image using a 3 × 3 averaging kernel
def blur_image(src, copy, h, w, c):
    """blurs an image using a 3 × 3 averaging kernel only with pure python. 

        Args:
            src(numpy.array): 3-dimensional numpy array of clear image
            copy(numpy.array): empty 3-dimensional numpy array for blurred image
            h(int): heigth of clear image
            w(int): width of clear image
            c(int): channel of clear image

        Return:
            copy(numpy.array): 3-dimensional numpy array for blurred src image

    """
    box_blur = 1./9.
    for i in range(h):
        for j in range(w):
            for k in range(c):
                if i == 0 and j == 0:
                    copy[i, j, k] = (src[i, j, k] + src[i, j, k] + src[i+1, j, k]
                    + src[i, j, k] + src[i, j+1, k] + src[i, j, k]
                    + src[i, j+1, k] + src[i+1, j, k] + src[i+1, j+1, k])
                elif i == 0:
                    copy[i, j, k] = (src[i, j, k] + src[i, j, k] + src[i+1, j, k]
                    + src[i, j-1, k] + src[i, j+1, k] + src[i, j-1, k]
                    + src[i, j+1, k] + src[i+1, j-1, k] + src[i+1, j+1, k])
                elif j == 0:
                    copy[i, j, k] = (src[i, j, k] + src[i-1, j, k] + src[i+1, j, k]
                    + src[i, j, k] + src[i, j+1, k] + src[i-1, j, k]
                    + src[i-1, j+1, k] + src[i+1, j, k] + src[i+1, j+1, k])
                else:
                    copy[i, j, k] = (src[i, j, k] + src[i-1, j, k] + src[i+1, j, k]
                    + src[i, j-1, k] + src[i, j+1, k] + src[i-1, j-1, k]
                    + src[i-1, j+1, k] + src[i+1, j-1, k] + src[i+1, j+1, k]) 

       
    return copy*box_blur

def writeTime(time, filename):
    """Writes the time the method blur_image uses to a file.

        Args:
            time(int): calculation of the time in seconds.
            filename(string): report filename.

    """
    f = open("report2.txt", "a")
    f.write("\nFilename: " + filename + "\nComputation time using pure python: " + str(time) + "seconds\n\n")
    f.close()


if __name__ == "__main__":
    main()

 