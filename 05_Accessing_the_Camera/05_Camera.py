import cv2
import sys

s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

source = cv2.VideoCapture(s)

win_name = 'Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

while cv2.waitKey(1) != 27:  # Escape key (ASCII 27) to exit
    has_frame, frame = source.read()
    
    if not has_frame:
        print("Frame not captured! Exiting loop.")
        break
    
    print("Frame captured successfully!")  # Debugging statement
    cv2.imshow(win_name, frame)

source.release()
cv2.destroyWindow(win_name)
