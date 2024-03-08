from skimage import io
import os

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename)
        if os.path.isfile(img_path):
            img = io.imread(img_path)
            if img is not None:
                images.append(img)
    return images