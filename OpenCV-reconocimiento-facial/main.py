from clasificador import detectorDeCaras
from renderer import render

imagePath = './test_images/' + 'personas.jpg'

render(detectorDeCaras(imagePath))
# gender, mood and face detector using OpenCV and Python
