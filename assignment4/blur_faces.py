#!/usr/bin/env python3
import numpy
import cv2
from blur_package import blur_1


def main():
    """Program for blurring faces in a image using the method in package_blur.blur_1.py.
    The program makes two imagefiles, one with rectangles to show that the face is 
    detected and one only with the blurred faces. The file with only the blurred faces
    is used to see if i managed to trick the face detector. It took about 15-20
    replications to trick it."
    """
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    src = cv2.imread("beatles.jpg")
    dst = src.copy()

    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.025, minNeighbors=5, minSize=(30, 30))


    print("Found {} faces!".format(len(faces)))

    if len(faces) != 0: 
        for (x, y, w, h) in faces:
            cv2.rectangle(src, (x, y), (x + w, y + h), (0, 255, 0), 2)
            #Finds the faces to blur in the image.
            sub_face = dst[y:y+h, x:x+w]
            h, w, c = sub_face.shape
            copy = numpy.empty(sub_face.shape)
            sub_face = numpy.pad(sub_face, ((1,1),(1,1),(0,0)), mode='edge')
            sub_face = sub_face.astype("uint32")
            #Blur each face.
            sub_face = blur_1.blur_image(sub_face, copy, h, w, c)
            sub_face = sub_face.astype("uint8")
            dst[y:y+sub_face.shape[0], x:x+sub_face.shape[1]] = sub_face

    cv2.imwrite("detected_faces.jpg", src)

    cv2.imwrite("blurred_faces.jpg", dst)


main()