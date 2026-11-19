
from pathlib import Path
import yaml
import math

dataset_valid = True
invalid_count = 0


with open("data/dataset/data.yaml", "r") as file:
    config = yaml.safe_load(file)

print("Number of classes:", config["nc"])
print("Class names:", config["names"])


if config["nc"] != len(config["names"]):
    print("ERROR: Number of classes does not match class names.")
    dataset_valid = False


splits = {
    "train": (
        Path("data/dataset/train/images"),
        Path("data/dataset/train/labels")
    ),
    "valid": (
        Path("data/dataset/valid/images"),
        Path("data/dataset/valid/labels")
    ),
    "test": (
        Path("data/dataset/test/images"),
        Path("data/dataset/test/labels")
    )
}

all_labels = []

# 3. Check image-label matching
for split_name, (image_dir, label_dir) in splits.items():

    if not image_dir.is_dir() or not label_dir.is_dir():
        print(f"ERROR: Missing folder in {split_name}")
        dataset_valid = False
        continue

    images = (
        list(image_dir.glob("*.jpg")) +
        list(image_dir.glob("*.jpeg")) +
        list(image_dir.glob("*.png"))
    )

    labels = list(label_dir.glob("*.txt"))

    image_stems = {image.stem for image in images}
    label_stems = {label.stem for label in labels}

    missing_labels = image_stems - label_stems
    missing_images = label_stems - image_stems

    print(f"\n{split_name.upper()} DATASET")
    print("Images:", len(images))
    print("Labels:", len(labels))
    print("Images without labels:", missing_labels)
    print("Labels without images:", missing_images)

    if missing_labels or missing_images:
        dataset_valid = False

    all_labels.extend(labels)



for label in all_labels:

    content = label.read_text()
    lines = content.splitlines()

    for line_number, line in enumerate(lines, start=1):

        values = line.split()

        line_valid = True

        if len(values) != 5:
            print(f"Invalid format: {label.name}, line {line_number}")
            dataset_valid = False
            invalid_count += 1
            continue

        try:
            class_id = int(values[0])

            x_center = float(values[1])
            y_center = float(values[2])
            width = float(values[3])
            height = float(values[4])

        except ValueError:
            print(f"Non-numeric annotation: {label.name}, line {line_number}")
            dataset_valid = False
            invalid_count += 1
            continue

        # Check class ID
        if not (0 <= class_id < config["nc"]):
            print(f"Invalid class ID: {label.name}, line {line_number}")
            line_valid = False

        # Check finite numeric values
        coordinates = [x_center, y_center, width, height]

        if not all(math.isfinite(value) for value in coordinates):
            print(f"Non-finite coordinate: {label.name}, line {line_number}")
            line_valid = False

        else:
            # Check normalized coordinates
            if not (0 <= x_center <= 1):
                print(f"Invalid x_center: {label.name}, line {line_number}")
                line_valid = False

            if not (0 <= y_center <= 1):
                print(f"Invalid y_center: {label.name}, line {line_number}")
                line_valid = False

            if not (0 < width <= 1):
                print(f"Invalid width: {label.name}, line {line_number}")
                line_valid = False

            if not (0 < height <= 1):
                print(f"Invalid height: {label.name}, line {line_number}")
                line_valid = False

            # Check bounding box boundaries
            if (
                x_center - width / 2 < 0 or
                x_center + width / 2 > 1 or
                y_center - height / 2 < 0 or
                y_center + height / 2 > 1
            ):
                print(f"Bounding box outside image: {label.name}, line {line_number}")
                line_valid = False

        if not line_valid:
            dataset_valid = False
            invalid_count += 1


# 5. Final report
print("\n========== DATASET REPORT ==========")
print("Invalid annotation lines:", invalid_count)

if dataset_valid:
    print("DATASET VALIDATION: PASS")
else:
    print("DATASET VALIDATION: FAIL")
