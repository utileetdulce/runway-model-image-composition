import random
from PIL import Image
import numpy as np
import cv2

class Image_composition():

    # Generate an image based on some text.
    def run_on_input(self, background_image, foreground_image):

        # Resize foreground to background
        (width, height) = (background_image.width, background_image.height)
        foreground_image = foreground_image.resize((width, height))

        # Split png foreground image
        b,g,r,a = cv2.split( np.array(foreground_image))

        # Save the foregroung RGB content into a single object
        foreground = cv2.merge((b,g,r))

        # Save the alpha information into a single Mat
        alpha = cv2.merge((a,a,a))

        # Read background image
        background = np.array(background_image)

        # Convert uint8 to float
        foreground = foreground.astype(float)
        background = background.astype(float)
        alpha = alpha.astype(float)/255

        # Perform alpha blending
        foreground = cv2.multiply(alpha, foreground)
        background = cv2.multiply(1.0 - alpha, background)
        outImage = cv2.add(foreground, background)

        return outImage
