#!/usr/bin/env python3
import numpy
import cv2
import time
import sys

#(H, W, C) heigth, width, channels

'''
main:
line 24: if len(sys.argv) == 3: --> if len(sys.argv) >= 2:, no need for an output filename to set the image you want to blur

blur_image_numpy():
edited the slicing on the output image so you dont lose a row on the top, bottom and sides
removed some unnecessary parameters from the slicing
'''

def main():
    """Main fuction to start the program. Reads the image from either the command inputfilename or 
    the default filename "beatles.jpg" and calls the blur_image method. It also saves the image to either 
    the command outputfilename or the default filename "blurred_image2.
    
    """
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print("set image to blur as 'beatles.jpg'")
        filename = "beatles.jpg"
    src = cv2.imread(filename)
    #halves the dimensions of the image
    #src = cv2.resize(src, (0, 0), fx=0.5, fy=0.5)
    h, w, c = src.shape
    #Set the shape to the same as in blur_1
    copy = numpy.empty((h+2, w+2, c))

    src = src.astype("uint32")

    #Call method for blurring image
    startTime = time.time()
    dst = blur_image_numpy(src, copy)
    endTime = time.time()
    #writeTime(endTime-startTime, filename)

    dst = dst.astype("uint8")
    if len(sys.argv) == 3:
        cv2.imwrite(sys.argv[2], dst)
    else: 
        print("Saved blurred image as 'blurred_image2.jpg'\n\nTo specify input-/",
        "outputfile use: blur.py [-h] blur_program input_filename output_filename\n")
        cv2.imwrite("blurred_image2.jpg", dst)
    

#Blur image using a 3 × 3 averaging kernel

def blur_image_numpy(src, copy):
    """blurs an image using a 3 × 3 averaging kernel with numpy computation. 

        Args:
            src(numpy.array): 3-dimensional numpy array of clear image.
            copy(numpy.array): empty 3-dimensional numpy array for blurred image.

        Return:
            copy(numpy.array): 3-dimensional numpy array for blurred src image.

    """
    h, w, c = copy.shape
    box_blur = 1./9.
    copy[2:h, 2:w] += src
    copy[2:h, 1:w-1] += src
    copy[2:h, 0:w-2] += src
    copy[1:h-1, 2:w] += src
    copy[1:h-1, 1:w-1] += src
    copy[1:h-1, 0:w-2] += src
    copy[0:h-2, 2:w] += src
    copy[0:h-2, 1:w-1] += src
    copy[0:h-2, 0:w-2] += src
    copy *= box_blur

    return copy[1:h-1, 1:w-1]

def writeTime(time, filename):
    """Writes the time the method blur_image uses to a file.

        Args:
            time(int): calculation of the time in seconds.
            filename(string): report filename.

    """
    f = open("report2.txt", "a")
    f.write("Filename: " + filename + "\nComputation time using numpy: " + str(time) + "seconds\n\n")
    f.close()


if __name__ == "__main__":
    main()