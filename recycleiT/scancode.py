import cv2
from pyzbar.pyzbar import decode


def get_text(path):
    image = cv2.imread(path)

    detected_barcode = decode(image)

    return detected_barcode[0].data.decode('utf-8')
