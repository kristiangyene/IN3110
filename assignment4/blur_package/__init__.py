#!/usr/bin/env python3
import blur_1
import blur_2
import blur_3
import cv2

def blur_image(input_filename, output_filename=None):
    """Method which blurs an image using the blur_1.py fuction blur_image. 
    Args:
        input_filename(string): string
        output_filename(None, string): None or string
    Return:
        dst: numpy (unsigned) integer 3D array
    """
    src = cv2.imread(input_filename)
    h, w, c = src.shape
    copy = numpy.empty(src.shape)

    #Padding src-image to blur edges
    src = numpy.pad(src, ((1,1),(1,1),(0,0)), mode='edge')
    src = src.astype("uint32")

    #Call method that returns blurred image 
    dst = blir_1.blur_image(src, copy, h, w, c)
    #writeTime(endTime-startTime, filename)

    dst = dst.astype("uint8")
    if output_filename == None:
        cv2.imwrite("blurred_image1.jpg", dst)
    else:
        cv2.imwrite(output_filename, dst)
    return dst