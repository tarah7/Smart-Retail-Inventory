from pathlib import Path
import cv2
import matplotlib.pyplot as plt

image_path = Path("data/raw/shelf.jpeg")

if not image_path.exists():
    raise SystemExit(f"Image not found: {image_path.resolve()}")

image = cv2.imread(str(image_path))

if image is None:
    raise SystemExit("OpenCV failed to load the image")

print("Loaded successfully")
print(f"Shape: {image.shape}")
print(f"Dimensions: {image.ndim}")
print(f"Data type: {image.dtype}")
print("Minimum pixel:", image.min())
print("Maximum pixel:", image.max())

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_image)
plt.title("Original Image")
plt.axis("off")
plt.show()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")
plt.show()

resized_image = cv2.resize(
    image,
    (640, 480),
    interpolation=cv2.INTER_AREA
)
resized_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
print("Resized shape:", resized_image.shape)
plt.imshow(resized_rgb)
plt.title("Resized Image")
plt.axis("off")
plt.show()

cropped_image = image[100:300, 200:600]

if cropped_image.size == 0:
    raise SystemExit("Crop is empty")

cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
print("Cropped shape:", cropped_image.shape)
plt.imshow(cropped_rgb)
plt.title("Cropped Image")
plt.axis("off")
plt.show()