import mediapipe as mp
import math
import cv2
from cv2 import cvtColor

cap     = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands   = mpHands.Hands()
mpDraw  = mp.solutions.drawing_utils


def getHandMove(hand_landmarks) -> str:
    landmarks = hand_landmarks.landmark
    if all([handLms.landmark[i].y < handLms.landmark[i + 3].y for i in range(9, 20, 4)]):
        return "rock"
    elif landmarks[13].y < landmarks[16].y and landmarks[17].y < landmarks[20].y:
        return "scissors"
    else:
        return "paper"


while True:
    success, image = cap.read();

    if not success:
        print("    <{@}> Camera not found");
        exit(1);
    
    imageRGB = cv2.cvtColor(
        src=image, 
        code=cv2.COLOR_BGR2RGB
    );
    results = hands.process(imageRGB);

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for _id, lm in enumerate(handLms.landmark):

                h, w, c = image.shape;
                cx, cy = int(lm.x * w), int(lm.y * h);

                if _id == 8:
                    cv2.circle(
                        image, 
                        (cx, cy), 
                        25, 
                        (255, 0, 255),
                        cv2.FILLED
                    );
                    mpDraw.draw_landmarks(
                        image, 
                        handLms, 
                        mpHands.HAND_CONNECTIONS
                    );

                    print(getHandMove(handLms));

    cv2.imshow("Output", image);
    cv2.waitKey(1);