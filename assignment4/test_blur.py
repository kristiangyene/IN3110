#!/usr/bin/env python3
import pytest
from blur_package import blur_1
import numpy

'''
made the tests work with the changes in the functions from blur_1, blur_2 and blur_3
set the upper limit in numpy.random.randint to 256 since its exclusive
'''

def test_maximum_value_of_array():
    """Test to make sure the maximum value of the array has decreased after blurring.

    """
    errorMessage = "Maximum value for the blurred image is bigger or equal to the  input image"
    randomArray = numpy.random.randint(0, 256, size=(480, 640, 3))
    maxval = numpy.amax(randomArray)
    h, w, c = randomArray.shape
    randomArray = numpy.pad(randomArray, ((1,1),(1,1),(0,0)), mode='edge')
    randomArray = randomArray.astype("uint32")
    dst = blur_1.blur_image(randomArray, h, w, c)
    assert maxval > numpy.amax(dst), errorMessage

def test_random_pixel():
    """Test to make sure a random pixel in the blurred image is the average of its 
    neighbors in the clear image.

    """
    errorMessage = "the pixel in blurred image is not the average of its neighbors in the clear image."
    randomArray = numpy.random.randint(0, 256, size=(480, 640, 3))
    h, w, c = randomArray.shape
    randomArray = numpy.pad(randomArray, ((1,1),(1,1),(0,0)), mode='edge')
    randomArray = randomArray.astype("uint32")
    dst = blur_1.blur_image(randomArray, h, w, c)
    assert int(dst[5, 3, 1]) == int((randomArray[5, 3, 1] + randomArray[5-1, 3, 1] + randomArray[5+1, 3, 1]
                    + randomArray[5, 3-1, 1] + randomArray[5, 3+1, 1] + randomArray[5-1, 3-1, 1]
                    + randomArray[5-1, 3+1, 1] + randomArray[5+1, 3-1, 1] + randomArray[5+1, 3+1, 1])/9), errorMessage

    assert int(dst[120, 320, 1]) == int((randomArray[120, 320, 1] + randomArray[120-1, 320, 1] + randomArray[120+1, 320, 1]
                    + randomArray[120, 320-1, 1] + randomArray[120, 320+1, 1] + randomArray[120-1, 320-1, 1]
                    + randomArray[120-1, 320+1, 1] + randomArray[120+1, 320-1, 1] + randomArray[120+1, 320+1, 1])/9), errorMessage