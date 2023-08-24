import cv2

def detectorDeCaras(imagePath):
    image = cv2.imread(imagePath)

    rectanguloEnCara(
        image, 
        cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )
    )
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    return img_rgb


def rectanguloEnCara(image, face_classifier):

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    face = face_classifier.detectMultiScale(
        gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
    )

    for (x, y, w, h) in face:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 4)
    
    return image
