import matplotlib.pyplot as plt

def render(image):
    plt.figure(figsize=(20,10))
    plt.imshow(image)
    plt.axis('off')

    plt.show()