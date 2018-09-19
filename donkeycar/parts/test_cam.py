import numpy as np
from skimage import io
from skimage import color
import matplotlib.pyplot as plt


img = io.imread('test.jpg')


img_hsv = color.rgb2hsv(img) # Image into HSV colorspace
h = img_hsv[:,:,0] # Hue
s = img_hsv[:,:,1] # Saturation
v = img_hsv[:,:,2] # Value aka Lightness

mask = (h > 10).astype(np.uint8)

plt.figure(1, figsize=(15, 15))

plt.subplot(4,2,1); plt.imshow(mask); plt.title('Hue')
plt.subplot(4,2,2); plt.imshow(s, cmap='gray'); plt.title('Saturation')
plt.subplot(4,2,3); plt.imshow(v, cmap='gray'); plt.title('Value')
plt.tight_layout()
plt.show()

mask = (s > 0.35).astype(np.uint8);  # Thresholding in the Saturation-channel
plt.subplot(4,2,4); plt.imshow(mask); plt.title('mask')

# disk_elem = disk(1) # Remove small regions
# opened = opening(mask, selem=disk_elem)
# plt.subplot(4,2,5); plt.imshow(opened); plt.title('Opened mask')

# square_elem = square(2) # rejoin colored features
# dilated = dilation(opened, selem=square_elem)
# plt.subplot(4,2,6); plt.imshow(dilated); plt.title('Opened mask')

# img2 = img.copy()
# img2[dilated.astype(bool), :] = 0; # Set the pixels to zero, where 
# plt.subplot(4,2,7); plt.imshow(img2); plt.title('Final Image') 