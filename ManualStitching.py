from GetPoints import *
from ComputeHomographyMatrix import *

import numpy as np
import cv2


video_path_1   = 'rtsp://112.133.197.90:2555/1/h264major'  #-> zoomed in
video_path_2 = 'rtsp://admin:admin@123@112.133.197.90:2554/cam/realmonitor?channel=1&subtype=1'  #-> wide

vid_1 = cv2.VideoCapture(video_path_1)
vid_2 = cv2.VideoCapture(video_path_2)

ret_1 , img1 = vid_1.read()
ret_2, img2 = vid_2.read()



select_keypts(img2, img1)
A, B = np.load("./params/A.npy"), np.load("./params/B.npy")
H = homographic_matrix(B,A)
np.save("./params/H.npy", H)
print("Homography matrix has been stored")
print(H)