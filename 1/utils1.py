from skimage import io
import matplotlib.pyplot as plt
import os

def load_images_from_folder(folder):
    images = []
    for filename in sorted(os.listdir(folder)):
        img_path = os.path.join(folder, filename)
        if os.path.isfile(img_path):
            img = io.imread(img_path)
            if img is not None:
                images.append(img)
    return images


def print_image(image, title):
    plt.tight_layout()
    plt.subplot(1, 2, 1)
    plt.imshow(image)
    plt.title(title)
