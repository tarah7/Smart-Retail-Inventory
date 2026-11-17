import cv2
import matplotlib.pyplot as plt
image=cv2.imread("data/raw/shelf.jpg")
if image is None:
    raise SystemExit ("image not found")
else:
    print("loaded successfully")
    print(f"shape:{image.shape} dimension:{image.ndim} data type:{image.dtype}")
    rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    plt.imshow(rgb)
    plt.show()

    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    plt.imshow(gray,cmap="gray")
    plt.show()

    resize=cv2.resize(image,(640,480))
    re=cv2.cvtColor(resize,cv2.COLOR_BGR2RGB)
    print("shape:",resize.shape)
    plt.imshow(re)
    plt.show()

    crop=image[100:200,200:600]
    if crop.size == 0:
        raise SystemExit("no image")
    else:
        cr=cv2.cvtColor(crop,cv2.COLOR_BGR2RGB)
        print("shape:",crop.shape)
        plt.imshow(cr)
        plt.show()