import imageio.v3 as iio
from PIL import Image
import numpy as np

filenames = ['picture1.png', 'picture2.png', 'picture3.png']
images = []

for filename in filenames:
    img = Image.open(filename).convert("RGB")  # Convert to 3-channel RGB
    images.append(np.array(img))  # Ensure same shape and channels

iio.imwrite('team.gif', images, duration=500, loop=0)
