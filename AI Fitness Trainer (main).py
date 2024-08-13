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


=================================================================================================================
#POSE MODULE for Pose detection (save it as another .py file):

import math
import cv2
import mediapipe as mp
import time
import numpy as np



class poseDetector():
    def __init__(self ,mode=False , upBody = False , smooth = True , detectionCon = 0.5 , trackingCon = 0.5):
        self.mode = mode
        self.upBody =upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackingCon = trackingCon
        self.trackingCon = trackingCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose()

    def findPose(self , img ,draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosittion(self , img , draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                #print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
        return self.lmList

    def findAngle(self , img , p1, p2 , p3 , draw = True):       #p1,p2,p3 are the indexes on which angle will be found

        #get the landmarks
        x1, y1 = self.lmList[p1][1:]                          #[1:] is used for slicing like [a,b,c] will give [b,c] as output
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]

        #calculate the angle
        angle =math.degrees(math.atan2(y3-y2 ,x3-x2) - math.atan2(y1-y2 , x1-x2))

        if angle<0 :
            angle += 360
        #print(angle)


        #draw
        if draw:
            cv2.line(img, (x1,y1) , (x2,y2) ,  (255,255,255), 3)
            cv2.line(img, (x3,y3) , (x2,y2) ,  (255,255,255), 3)
            cv2.circle(img, (x1, y1), 10, (245, 117 , 66), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (245,66,230), 2)
            cv2.circle(img, (x2, y2), 10, (245, 117 , 66), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (245,66,230), 2)
            cv2.circle(img, (x3, y3), 10, (245, 117 , 66), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (245,66,230), 2)
            cv2.putText(img , str(int(angle)) , (x2-50 , y2 +50) , cv2.FONT_HERSHEY_PLAIN , 2 , (0,0,255) , 2)

        return angle



cap = cv2.VideoCapture(0)
count = 0  # count the no. of reps
dir = 0    # 0 for up and 1 for down and count will increase only when dir becomes both 1 & 0 i.e., up & down.
pTime = 0
stage = None              #declared for direction
detector = poseDetector()
while True:
    success, img = cap.read()
    #img  = cv2.imread('dips.jpg')
    img = cv2.resize(img, (1200, 900))
    img = detector.findPose(img , False)
    lmList = detector.findPosittion(img , draw = False)
    if len(lmList) != 0:
        #print(lmList[14])
        #cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)
        # right arm
        #detector.findAngle(img , 11,13,15)       # 11,13,15 are the indexes of the right hand
        # left arm
        angle = detector.findAngle(img, 11,13,15)  # 12,14,16 are the indexes of the left hand
        per = np.interp(angle, (210, 310), (0, 100))  # (210,310) is the range of angles min and max
        bar = np.interp(angle, (220, 310), (650, 100))
        # print(angle,per)

    # check for dumbell curls
    color = (255, 0, 0)  # purple color
    if per == 100:
        stage = "Down"
        color = (0, 255, 0)  # green color overrides purple color
        if dir == 0:
            count += 0.5
            dir = 1
    if per == 0 and stage=="Down":
        stage = "Up"
        color = (0, 255, 0)
        if dir == 1:
            count += 0.5
            dir = 0
    print(count)

    # drawing bar
    cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
    cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
    cv2.putText(img, f'{int(per)}%', (1060, 75), cv2.FONT_HERSHEY_PLAIN, 5, color, 5)


    # count curls
    cv2.rectangle(img, (0,500), (250,720), (255,255,255), cv2.FILLED)
    cv2.putText(img, f'Count:{str(int(count))}' , (10, 670), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)
    cv2.putText(img, f'direction:{str(stage)}', (10, 600), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 4)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img , f'fps: {int(fps)}',(70,50) ,cv2.FONT_HERSHEY_PLAIN , 3 , (255,0,0) ,3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)


