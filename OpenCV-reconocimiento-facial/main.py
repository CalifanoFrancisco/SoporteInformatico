from clasificador import clasificador
from renderer import render


image_path = 'test_images/' + 'personas.jpg'

img = clasificador(image_path)

render(img)



