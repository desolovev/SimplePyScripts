#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import cv2

img = cv2.imread('example.jpg')
cv2.imshow('img', img)

# Invert
img_invert = cv2.bitwise_not(img)
cv2.imshow('img_invert', img_invert)

# Gray
img_invert_gray = cv2.cvtColor(img_invert, cv2.COLOR_BGR2GRAY)
cv2.imshow('img_invert_gray', img_invert_gray)

cv2.waitKey()