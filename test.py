from cv2.cv import *


camera = CreateFileCapture("rtsp://vesa:lollero@192.168.0.102:88/videoMain")

if (camera == NULL) :
	exit()

NamedWindow("img")

while (waitKey(100) != 27):
	img = QueryFrame(camera)
	ShowImage("img", img)

ReleaseCapture(camera)


