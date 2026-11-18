import cv2
import matplotlib.pyplot  as plt
from pathlib import Path

image_path= Path("data/raw/shelf.jpeg")

if not image_path.exists():
    raise SystemExit("image is not exist")

image= cv2.imread(str(image_path))

if image is None:
    raise SystemExit("OpenCV failed to load the image")

hsv= cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

hue= hsv[:,:,0]
saturation= hsv[:,:,1]

h_hist= cv2.calcHist([hsv],[0],None,[180],[0,180])
s_hist= cv2.calcHist([hsv],[1],None,[256],[0,256])

gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edge= cv2.Canny(gray_image,100,200)
rgb_image= cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

plt.subplot(2,2,1)
plt.imshow(rgb_image)
plt.title("original image")
plt.axis("off")

plt.subplot(2,2,2)
plt.plot(h_hist)
plt.title("Hue histogram")
plt.xlabel("Hue value")
plt.ylabel("Pixel count")

plt.subplot(2,2,3)
plt.plot(s_hist)
plt.title("Saturation histogram")
plt.xlabel("Saturation value")
plt.ylabel("Pixel count")

plt.subplot(2,2,4)
plt.imshow(edge,cmap="gray")
plt.title("Canny edge image")
plt.axis("off")

plt.tight_layout()
plt.show()