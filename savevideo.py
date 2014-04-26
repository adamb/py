import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fps = 15
capSize = (640,480)
fourcc = cv2.cv.CV_FOURCC('m','p','4','v')
out = cv2.VideoWriter()
suc = out.open('output.mov',fourcc, fps, capSize,True)

while(cap.isOpened()):
    ret, frame = cap.read()
    width = np.size(frame, 1) #here is why you need numpy!  (remember to "import numpy as np")
    height = np.size(frame, 0)
    print width, height
    if ret==True:
        # frame = cv2.flip(frame,0)

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
