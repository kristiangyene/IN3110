#!/usr/bin/env python3
import argparse
import cv2
import numpy as np
import os 
import blur_1
import blur_2
import blur_3


"""For this command line user interface I chose to make the arguments required.

"""


'''
made the implementation use the modules instead of os.system()
'''

parser = argparse.ArgumentParser(
    description="Blur image script"
)
parser.add_argument('blur_program', help="Type of blur program: blur_1, blur_2, blur_3", type=str, choices={"blur_1", "blur_2", "blur_3"})
parser.add_argument('input_filename', help="Name of input filename for image", type=str)
parser.add_argument('-o', '--output_filename', help="Name of output filename for blurred image", type=str)
args = parser.parse_args()
inputFile = args.input_filename
outputFile = args.output_filename
program = args.blur_program

img = cv2.imread(args.input_filename)
h,w,c = img.shape
src = np.pad(img, ((1,1),(1,1),(0,0)), mode='edge').astype("uint32")
copy = np.zeros((h+2,w+2,c))

if args.blur_program == "blur_1":
    dst = blur_1.blur_image(src, h,w,c).astype("uint8")
elif args.blur_program == "blur_3":
    dst = blur_3.blur_image_numba(src, h, w, c).astype("uint8")
else:
    dst = blur_2.blur_image_numpy(src, copy).astype("uint8")

if args.output_filename:
    cv2.imwrite(args.output_filename, dst)


#os.system('python3 ' + program + '.py ' + inputFile + '.jpg ' + outputFile + '.jpg')

