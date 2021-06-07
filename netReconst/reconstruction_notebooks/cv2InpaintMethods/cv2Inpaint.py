import numpy as np
from matplotlib import pyplot as plt
import cv2
from cv2 import imwrite
from PIL import Image, ImageChops
# src: https://math.berkeley.edu/~sethian/2006/Explanations/fast_marching_explain.html
img = cv2.imread('damage.png')  # input
mask = cv2.imread('mask.png',0)    # mask

dst_TELEA = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)
dst_NS = cv2.inpaint(img,mask,3,cv2.INPAINT_NS)
cv2.imwrite('telea.png', dst_TELEA)
cv2.imwrite('NS.png', dst_NS)

plt.subplot(221), plt.imshow(img)
plt.title('degraded image')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.title('mask image')
plt.subplot(223), plt.imshow(dst_TELEA)
plt.title('TELEA')
plt.subplot(224), plt.imshow(dst_NS)
plt.title('NS')

plt.tight_layout()
plt.show()
original = cv2.imread('original.png',0)
telema = cv2.imread('telea.png',0)
NS = cv2.imread('NS.png',0)

# first algo
# compute difference
# assign images
original = Image.open("original.png")
telema = Image.open("telea.png")
NS = Image.open("NS.png")

# finding difference
diff = ImageChops.difference(original, telema)
# showing the difference
diff.show(title='telema from original')

# finding difference
diff = ImageChops.difference(original, NS)

# showing the difference
diff.show(title='NS from original')
