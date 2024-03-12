import cvzone
import cv2
from cvzone.PoseModule import PoseDetector
import streamlit as st
import streamlit_webrtc
from streamlit_webrtc import webrtc_streamer

# def showTrain(videoPath):
#     # vid = cv2.VideoCapture(videoPath)
#     # st.camera_input(label='Your Turn :)',disabled=False)
#     while True:
#         _, img = cap.read()
#         cv2.imshow("Train tutorial", img)

def myTrAiner(exercise):
    if (exercise == "squat"):
        cap = cv2.VideoCapture(0)# write your video path or 0 for webcam
        # '/Users/ahmedbawazeer/Downloads/train.mov'
        # Initialize the PoseDetector class with the given parameters
        # cap = webrtc_streamer(key="example")
        aa = st.empty() #To show the webcam
        detector = PoseDetector(staticMode=False,
                                modelComplexity=1,
                                smoothLandmarks=True,
                                enableSegmentation=True,
                                smoothSegmentation=True,
                                detectionCon=0.7,
                                trackCon=0.4)

        SP = "Starting Position"  # Text for Starting Position (SP)
        BP = "Correct Back Position!!"  # Text for Back Position (BP)
        KP = "Correct Knee Position!!"  # Text for Knee Position (KP)
        IBP = "Incorrect Back Position!!"  # Text for Incorrect Back Position (IBP)
        IKP = "Incorrect Knee Position!!"  # Text for Incorrect Knee Position (IKP)

        font = cv2.FONT_HERSHEY_SIMPLEX  # Font type
        fontScale = 1  # Font scale (size of the font)
        RP = (0, 255, 0)  # (BGR) Color of the Right Pose (RP)
        WP = (0, 0, 255)  # (BGR) Color of the Wrong Pose (WP)
        thickness = 3  # Thickness of the lines used to draw the text

        # CR = 0 #Counter for correct reps

        # Loop to continuously get frames from the webcam
        while True:
            # Capture each frame from the webcam and flip the photo
            success, img = cap.read()
            img = cv2.flip(img,1) # uncomment this line when using webcam

            # Find human pose in the frame
            img = detector.findPose(img)

            # Find the landmarks, bounding box, and center of the body in the frame
            lmList, bboxInfo = detector.findPosition(img, draw=False, bboxWithHands=False)

            # Check if any body landmarks are detected
            if lmList:
        
                if (lmList[23][2] > lmList[24][2]) :
                    # Calculate the Left Knee angle and draw it on the image
                    LKnee_angle, img = detector.findAngle(lmList[24][0:2],
                                                    lmList[26][0:2],
                                                    lmList[28][0:2],
                                                    img=img,
                                                    color=(0, 0, 255),
                                                    scale=2)
                    LBack_angle, img = detector.findAngle(lmList[12][0:2],
                                                        lmList[24][0:2],
                                                        lmList[26][0:2],
                                                        img=img,
                                                        color=(0, 0, 255),
                                                        scale=2)
                    
                    if ((LBack_angle>175 and LBack_angle <= 185)): 
                        cv2.putText(img, SP, (50, 50), font, fontScale, (255, 0, 0), thickness, cv2.LINE_AA)
                    
                    #Checking if the Back and Knee position is Incorrect and wrtie a message on the screen   
                    # Adding  ( ^ (LBack_angle>295 or LBack_angle < 280)) to the condetion to detect the left side
                    elif ((LBack_angle>85 or LBack_angle <= 70)):
                        cv2.putText(img, IBP, (50, 100), font, fontScale, WP, thickness, cv2.LINE_AA)
                        # Adding  (  ^ (LKnee_angle>80 or LKnee_angle < 70)) to the condetion to detect the left side
                        if ((LKnee_angle>285 or LKnee_angle < 275)):
                            cv2.putText(img, IKP, (50, 150), font, fontScale, WP, thickness, cv2.LINE_AA)

                    #Checking if the Back and Knee position is correct and wrtie a message on the screen                   
                    elif ((LBack_angle>70 and LBack_angle <= 85)):
                        cv2.putText(img, BP, (50, 100), font, fontScale, RP, thickness, cv2.LINE_AA)
                        # Adding  (  ^ (LKnee_angle<80 and LKnee_angle >= 70)) to the condetion to detect the left side
                        if ((LKnee_angle<285 and LKnee_angle >= 275)):
                            cv2.putText(img, KP, (50, 150), font, fontScale, RP, thickness, cv2.LINE_AA)
                
                else:
                    # Calculate the Right Back angle and draw it on the image
                    RBack_angle, img = detector.findAngle(lmList[11][0:2],
                                                            lmList[23][0:2],
                                                            lmList[25][0:2],
                                                            img=img,
                                                            color=(0, 0, 255),
                                                            scale=2)

                    # Calculate the Right Knee angle and draw it on the image            
                    RKnee_angle, img = detector.findAngle(lmList[23][0:2],
                                                        lmList[25][0:2],
                                                        lmList[27][0:2],
                                                        img=img,
                                                        color=(0, 0, 255),
                                                        scale=2)
                    
                    #Checking if the setting position is correct and wrtie a message on the screen
                    # Adding( ^ LBack_angle>170 and LBack_angle <= 185) to the condetion to detect the left side
                    if ((RBack_angle>170 and RBack_angle <= 185)): 
                        cv2.putText(img, SP, (50, 50), font, fontScale, (255, 0, 0), thickness, cv2.LINE_AA)

                    #Checking if the Back and Knee position is Incorrect and wrtie a message on the screen   
                    # Adding  ( ^ (LBack_angle>295 or LBack_angle < 280)) to the condetion to detect the left side
                    elif ((RBack_angle>295 or RBack_angle < 280)):
                        cv2.putText(img, IBP, (50, 100), font, fontScale, WP, thickness, cv2.LINE_AA)
                        # Adding  (  ^ (LKnee_angle>80 or LKnee_angle < 70)) to the condetion to detect the left side
                        if ((RKnee_angle>80 or RKnee_angle < 70)):
                            cv2.putText(img, IKP, (50, 150), font, fontScale, WP, thickness, cv2.LINE_AA)

                    #Checking if the Back and Knee position is correct and wrtie a message on the screen                   
                    elif ((RBack_angle>280 and RBack_angle <= 295)):
                        cv2.putText(img, BP, (50, 100), font, fontScale, RP, thickness, cv2.LINE_AA)
                        # Adding  (  ^ (LKnee_angle<80 and LKnee_angle >= 70)) to the condetion to detect the left side
                        if ((RKnee_angle<80 and RKnee_angle >= 70)):
                            cv2.putText(img, KP, (50, 150), font, fontScale, RP, thickness, cv2.LINE_AA)
                        
            # Display the frame in a window
            # cv2.imshow("Image", img)
            aa.image(img , channels="BGR")

            # Wait for 1 millisecond between each frame
            if (cv2.waitKey(1) and 0xFF == (ord('q') or ord('Q'))):
                break

        cap.release()           
        cv2.destroyAllWindows()

