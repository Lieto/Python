import cv2

image = cv2.imread('test.jpg')
cv2.imwrite('koe.jpg', image)

grayImage = cv2.imread('test.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
cv2.imwrite('koegray.jpg', grayImage)

