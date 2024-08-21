# Install Pillow and then run the script
from PIL import Image, ImageEnhance, ImageFilter
import os

# Select the path of the folder containing the images you want to edit
path_in = "./Before_edition"

# And the path where you want to save the edited images
path_out = "/After_edition"

# Creating a loop allows us to apply the same changes to all images in the folder
for filename in os.listdir(path_in):

    # Open the image by joining the path with a slash and the filename
    image = Image.open(f"{path_in}/{filename}")

    # Apply the changes you want to make to the image
    ## With the sharpen filter, you can enhance the edges of the image, making it look with more definition
    edition = image.filter(ImageFilter.SHARPEN)

    ## With the contrast enhancer, you can increase the contrast of the image
    factor = 1.2
    Enhancer = ImageEnhance.Contrast(edition)
    edition = Enhancer.enhance(factor) # You can also write directly factor = 1.25 here.

    # Save the edited image in the output folder
    file_name = os.path.splitext(filename)[0]
    edition.save(f".{path_out}/{file_name}_edited.jpg")