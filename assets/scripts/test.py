#!/usr/bin/env python3

import cv2
import numpy as np
import sys
import time
from pyzbar import pyzbar

qrDecoder = cv2.QRCodeDetector()

img = cv2.imread("test.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(thresh, blackwhite) = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv[:, :, 2] += 200
# for x in range(0, len(hsv)):
#     for y in range(0, len(hsv[0])):
#         hsv[x, y][2] += 2
# img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# R, G, B = cv2.split(img)
# img_R = cv2.equalizeHist(R)
# img_G = cv2.equalizeHist(G)
# img_B = cv2.equalizeHist(B)
# img = cv2.merge((img_R, img_G, img_B))

img = blackwhite
cv2.imshow("img", img)
cv2.waitKey(0)

data, bbox, rectifiedimg = qrDecoder.detectAndDecode(img)
if len(data) > 0:
    print("Ddcoded data: {}".format(data))
    cv2.imshow("img", img)
    cv2.imshow("Rectified", np.uint8(rectifiedimg))
    cv2.waitKey(0)
else:
    print("QR Code not detected.")

    # R, G, B = cv2.split(img)
    # img_R = cv2.equalizeHist(R)
    # img_G = cv2.equalizeHist(G)
    # img_B = cv2.equalizeHist(B)

    # img2 = cv2.merge((img_R, img_G, img_B))

    # cv2.imshow("img", img2)
    # cv2.waitKey(0)
    barcodes = pyzbar.decode(img)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(
            img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2
        )

        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))

        cv2.imshow("Image", img)
        cv2.waitKey(0)

cv2.destroyAllWindows()

