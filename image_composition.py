import random
from PIL import Image
import numpy as np
import cv2

class Image_composition():

    # Generate an image based on some text.
    def run_on_input(self, background_image, foreground_image):
        background_image = background_image.resize(foreground_image.size)
        composite = Image.alpha_composite(background_image, foreground_image)
        return composite
