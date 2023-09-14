import cv2
import os

def detectorDeCaras(imagePath):
    image = cv2.imread(imagePath)

    cropFaces(image)
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    return img_rgb

def cropFaces(img):
    # convert to grayscale of each frames
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # read the haarcascade to detect the faces in an image
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    
    # detects faces in the input image
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    
    # loop over all detected faces
    clearDir('output')

    # if no faces are detected then chauchau 
    if len(faces) == 0: return

    for i, (x, y, w, h) in enumerate(faces):

       # To draw a rectangle in a face
       cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
       
       # Resizing the image
       face = img[y:y + h, x:x + w]
       
       # Save image to file
       cv2.imwrite(f'output/face_{i}.jpg', face)

def clearDir(dir):
    os.makedirs(dir, exist_ok=True)
    os.system(f'rm -rf {dir}/*')