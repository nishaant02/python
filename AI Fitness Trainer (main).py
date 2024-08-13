import cv2
import mediapipe as mp
import time
import posemodule as pm
import numpy as np

cap = cv2.VideoCapture(0)
detector = pm.poseDetector()
count = 0  # count the no. of reps
dir = 0    # 0 for up and 1 for down and count will increase only when dir becomes both 1 & 0 i.e., up & down.
pTime=0
stage = None              #declared for direction
while True:
    success , img =cap.read()
    img = cv2.resize(img, (1200, 900))
    img = cv2.imread(0)
    img = detector.findPose(img)
    lmList = detector.findPosittion(img, False)
    #print(lmList)
    if len(lmList) != 0:
        #right arm
        #detector.findAngle(img , 11,13,15)       # 11,13,15 are the indexes of the right hand
        # left arm
        angle = detector.findAngle(img, 11,13,15)  # 12,14,16 are the indexes of the left hand
        per = np.interp(angle , (210 , 310) , (0,100))               #(210,310) is the rangle of angles min and max
        bar = np.interp(angle , (220 , 310) , (650,100))
        #print(angle,per)

    #check for dumbell curls
    color =(255,0,0)   # purple color
    if per == 100:
        stage = "Down"
        color = (0,255,0)  #green color overrides purple color
        if dir == 0:
            count += 0.5
            dir = 1
    if per == 0 and stage=="Down":
        stage = "Up"
        color = (0, 255, 0)
        if dir ==1:
            count += 0.5
            dir = 0
    print(count)

    # drawing bar
    cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
    cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
    cv2.putText(img , f'{int(per)}%' , (1060,75) , cv2.FONT_HERSHEY_PLAIN , 5 , color ,5)

    # count curls
    cv2.rectangle(img , (0,500), (250,720), (0,255,0) , cv2.FILLED)
    cv2.putText(img , f'Count:{str(int(count))}' , (10,670) , cv2.FONT_HERSHEY_PLAIN , 3 , (255,0,0) ,5)
    cv2.putText(img, f'direction:{str(stage)}', (10, 600), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 4)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img , f'fps: {int(fps)}' , (50,100) , cv2.FONT_HERSHEY_PLAIN , 5 , (255,0,0) ,5)
    cv2.imshow("image",img)
    cv2.waitKey(1)
