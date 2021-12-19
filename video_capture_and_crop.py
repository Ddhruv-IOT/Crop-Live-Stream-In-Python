# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 19:13:30 2021

@author: ACER
"""
import cv2

stream = cv2.VideoCapture(1)

while 1:
    ret, frame = stream.read()
    cv2.imshow('Original Video', frame)
    cv2.imshow('Cropped Video', frame[100:400, 100:500])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

stream.release()
cv2.destroyAllWindows()
