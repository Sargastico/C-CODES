"""
Código para testes de visão computacional utilizando OpenCV.
"""

from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse
import random as rng

rng.seed(12345)

def thresh_callback(val): #Reconhece contornos, desenha bounding box e elipse.
    threshold = val

    canny_output = cv.Canny(src_gray, threshold, threshold * 2)

    contours, _ = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    contours_poly = [None] * len(contours)
    boundRect = [None] * len(contours)
    centers = [None] * len(contours)
    radius = [None] * len(contours)
    for i, c in enumerate(contours):
        contours_poly[i] = cv.approxPolyDP(c, 3, True)
        boundRect[i] = cv.boundingRect(contours_poly[i])
        centers[i], radius[i] = cv.minEnclosingCircle(contours_poly[i])

    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)

    for i in range(len(contours)):
        color = (rng.randint(0, 256), rng.randint(0, 256), rng.randint(0, 256))
        cv.drawContours(drawing, contours_poly, i, color)
        cv.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])), \
                     (int(boundRect[i][0] + boundRect[i][2]), int(boundRect[i][1] + boundRect[i][3])), color, 2)
        cv.circle(drawing, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), color, 2)

    return drawing


cap = cv.VideoCapture(1)

while (cap.isOpened()):
    # Capture frame-by-frame
    ret, src = cap.read()
    if ret:

        src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
        src_gray = cv.blur(src_gray, (3, 3))

        source_window = 'Source'
        cv.namedWindow(source_window)
        cv.imshow(source_window, src)
        max_thresh = 255
        thresh = 100  
        cv.createTrackbar('Canny thresh:', source_window, thresh, max_thresh, thresh_callback)
        draw = thresh_callback(thresh)
        # Display the resulting frame
        cv.imshow('src', src)
        cv.imshow('Source', draw)

        added_image = cv.addWeighted(src, 0.4, draw, 0.1, 0)
        cv.imshow('combined', added_image)

        if cv.waitKey(20) & 0xFF == ord('q'):
            break

cap.release()
cv.destroyAllWindows()
