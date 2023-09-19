from deepface import DeepFace
import cv2
import os

def clearDirectory(dir):
    os.makedirs(dir, exist_ok=True)
    os.system(f'rm -rf {dir}/*')
    
def clasificador(image_path):
    
    # load image
    img = cv2.imread(image_path)

    # convert to grayscale of each frames
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # read the haarcascade to detect the faces in an image
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # detects faces in the input image
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)

    # if no faces detected return
    if len(faces) == 0: return
    
    faces_information = DeepFace.analyze(img_path = image_path, actions=['emotion', 'gender', 'age'])

    # if models find different amount of faces
    if len(faces) != len(faces_information):
        return

    #print('Gender:', face['dominant_gender'], 'Mood:', face['dominant_emotion']);

    clearDirectory('output')

    for i, (x, y, w, h) in enumerate(faces):

       # To draw a rectangle in a face
       cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)

       # add text to image
       cv2.putText(
            img,
            'Gender:' + faces_information[i]['dominant_gender'] + ' ' +
            'Mood:'   + faces_information[i]['dominant_emotion'] + ' ' +
            'Age:'    + str(faces_information[i]['age']),
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (36,255,12),
            2,
            cv2.LINE_AA
        )
       
       # Resizing the image
       face = img[y:y + h, x:x + w]
       
       # Save image to file
       cv2.imwrite(f'output/face_{i}.jpg', face)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img_rgb;
