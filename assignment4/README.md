# Mandatory Assignment 4 - Basic Python programming

All files are tested on a ifi computer.

## General notice
I assume that the user have already installed everything needed for running these scripts.
Packages to be installed: numpy, numba, argparse, pytest

## 4.1: Python implementation

How to run blur_1:
```
# For running blur_1 with default filenames: "beatles.jpg" and "blurred_image1.jpg":
$ python3 blur_1.py

> set image to blur as 'beatles.jpg'
> Saved blurred image as 'blurred_image1.jpg'
> To specify input-/ outputfile use: blur.py [-h] blur_program input_filename output_filename

# If you want to choose the input filename and output filename: python3 blur_1 an_existing_image.jpg output_filename.jpg
$ python3 blur_1.py katt.jpg nytt_bilde.jpg
```

A file with the blurred image will be saved in the same directory.

## 4.2: Numpy implementation

Run the same way as in 4.1 but with blur_2.py instead.

```
$ python3 blur_2.py

> set image to blur as 'beatles.jpg'
> Saved blurred image as 'blurred_image2.jpg'
> To specify input-/ outputfile use: blur.py [-h] blur_program input_filename output_filename
```

A file with the blurred image will be saved in the same directory.

## 4.3: Numba implementation

Run the same way as in 4.1 but with blur_3.py instead.

```
$ python3 blur_3.py

> set image to blur as 'beatles.jpg'
> Saved blurred image as 'blurred_image3.jpg'
> To specify input-/ outputfile use: blur.py [-h] blur_program input_filename output_filename
```

A file with the blurred image will be saved in the same directory.

## 4.5 User interface

How to run blur:
```
# If you want to get the instructions:
$ python3 blur.py --help

> Usage: blur.py [-h] blur_program input_filename output_filename
...

# Example:
$ python3 blur.py blur_1 beatles new_image
# Then the blurred image of beatles.jpg will be saved as new_image.jpg
```

A file with the blurred image of the input_filename will be saved as the output_filename in the same directory.

### notice
I made a decision to make the command arguments required when executing blur.py

## 4.6 Packaging and unit tests

Run pytest:

```
$ pytest -v
```
NB: make sure you are in the right directory when executing.
If all tests succeed it will say "n tests passed in x seconds"

## 4.7 Blurring faces

run blur_faces:

```
$ python3 blur_faces
```
Blurred faces and detected faces are separated into to output images. To make both in one image simply change:
replace src with dst in cv2.rectangle(src, (x, y), (x + w, y + h), (0, 255, 0), 2)


