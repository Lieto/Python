import cv2
import numpy

#videoCapture = cv2.VideoCapture('test.avi')
#videoCapture = cv2.VideoCapture('rtsp://vesa:lollero@dt6288.myfoscam.org:88/videoMain')
#videoCapture = cv2.VideoCapture('test2.ts')
videoCapture = cv2.VideoCapture('koe.ts')

fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)
print fps

size = (int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
print size

msec = videoCapture.get(cv2.cv.CV_CAP_PROP_POS_MSEC)
print msec


fps = 7

videoWriter = cv2.VideoWriter('videoOut.avi', cv2.cv.CV_FOURCC('I', '4', '2', '0'), fps, size)

success, image = videoCapture.read()
#print success

while success:
    #videoWriter.write(image)
    cv2.imshow('test', image)
    msec = videoCapture.get(cv2.cv.CV_CAP_PROP_POS_MSEC)
    print msec
    success, image = videoCapture.read()


#cv2.waitKey(0)


#while cv2.waitKey(1):
#    if not videoCapture.grab():
#        break
#
    #image = videoCapture.retrieve()
#    image = videoCapture.read()
#    cv2.imshow('vidoetest', image)
    #koe = numpy.array(image)
    #cv2.cv.ShowImage("test", koe)
    
    
#if (videoCapture.isOpened() != 0):
#    print 'Cannot open the camera'
    
#fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)
#print fps

#size = (int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
#        int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
#print size

#videoWriter = cv2.VideoWriter('videoOut.avi', cv2.cv.CV_FOURCC('I', '4', '2', '0'), fps, size)

#success, frame = videoCapture.read()

#cv2.imwrite('vidoetest1.jpg', frame)

#while success:
#    videoWriter.write(frame)
#    success, frame = videoCapture.read()
    
