import numpy as np
import cv2

# capSize = (1028,720) # this is the size of my source video
# fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v') # note the lower case
# self.vout = cv2.VideoWriter()
# success = self.vout.open('output.mov',fourcc,fps,capSize,True)


cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fps = 15
fourcc = cv2.cv.CV_FOURCC('m','p','4','v')
out = cv2.VideoWriter()
suc = out.open('output.mov',fourcc, fps, (640,480),True)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
out = None
cv2.destroyAllWindows()
