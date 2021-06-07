from skimage.restoration import inpaint
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from PIL import Image, ImageChops
from skimage.util import compare_images

# src: https://scikit-image.org/docs/dev/auto_examples/applications/plot_image_comparison.html
# src: https://scikit-image.org/docs/dev/auto_examples/filters/plot_inpaint.html
# src: https://scikit-image.org/docs/stable/auto_examples/filters/plot_inpaint.html

damage = io.imread('damage.png')
mask = io.imread('mask.png')
original = io.imread('original.png')

image_result = inpaint.inpaint_biharmonic(damage, mask, multichannel=True)
#io.imsave('result.png',image_result)
fig, axes = plt.subplots(ncols=3, nrows=2)
ax = axes.ravel()
diff_rotated = compare_images(original, image_result, method='diff')
ax[0].set_title('Original image')
ax[0].imshow(original)

ax[1].set_title('Mask')
ax[1].imshow(mask, cmap=plt.cm.gray)

ax[2].set_title('Defected image')
ax[2].imshow(damage)

ax[3].set_title('Inpainted image')
ax[3].imshow(image_result)

ax[4].set_title('diff rotated')
ax[4].imshow(diff_rotated)

for a in ax:
    a.axis('off')

fig.tight_layout()
plt.show()