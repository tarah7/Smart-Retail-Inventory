from pathlib import Path
import yaml

dataset_valid = True
invalid_count = 0

with open("data/dataset/data.yaml","r") as file:
    config= yaml.safe_load(file)
print(config)
print(config["nc"])
print(config["names"])

train_img = Path("data/dataset/train/images")
train_lab= Path("data/dataset/train/labels")

train_images = list(train_img.glob("*.jpg"))+list(train_img.glob("*.jpeg"))+list(train_img.glob("*.png"))
train_labels= list(train_lab.glob("*.txt"))

train_img_set=set()
train_lab_set=set()

for image in train_images:
    train_img_set.add(image.stem)

for labe in train_labels:
    train_lab_set.add(labe.stem)

print(f"train-img:{train_img_set-train_lab_set}")
print(f"train-lab:{train_lab_set-train_img_set}")


valid_img = Path("data/dataset/valid/images")
valid_lab= Path("data/dataset/valid/labels")

valid_images = list(valid_img.glob("*.jpg"))+list(valid_img.glob("*.jpeg"))+list(valid_img.glob("*.png"))
valid_labels= list(valid_lab.glob("*.txt"))

valid_img_set=set()
valid_lab_set=set()

for image in valid_images:
    valid_img_set.add(image.stem)

for labe in valid_labels:
    valid_lab_set.add(labe.stem)

print(f"valid-img:{valid_img_set-valid_lab_set}")
print(f"valid-lab:{valid_lab_set-valid_img_set}")


test_img = Path("data/dataset/test/images")
test_lab= Path("data/dataset/test/labels")

test_images = list(test_img.glob("*.jpg"))+list(test_img.glob("*.jpeg"))+list(test_img.glob("*.png"))
test_labels= list(test_lab.glob("*.txt"))

test_img_set=set()
test_lab_set=set()

for image in test_images:
    test_img_set.add(image.stem)

for labe in test_labels:
    test_lab_set.add(labe.stem)

print(f"test-img:{test_img_set-test_lab_set}")
print(f"test-lab:{test_lab_set-test_img_set}")

for label in train_lab:
    label_path=Path(f"data/dataset/train/labels/{label}")
    content= label_path.read_text()
    lines=content.splitlines()
    for line in lines:
        values=line.split()
        class_id=int(values[0])
        x_center=float(values[1])
        y_center=float(values[2])
        width   =float(values[3])
        height  =float(values[4])
        try:
            if 0 <= class_id < config["nc"]:
                pass
        except ValueError:
            print("invalid class id")
            dataset_valid = False
            invalid_count += 1

        try:
            if 0 <= x_center <= 1:
                pass
        except ValueError:
            print("invalid x_center")
            dataset_valid = False
            invalid_count += 1

        try:
            if 0 <= y_center <= 1:
                pass
        except ValueError:
            print("invalid y_center")
            dataset_valid = False
            invalid_count += 1

        try:
            if 0 <= width <= 1:
                pass
        except ValueError:
            print("invalid width")
            dataset_valid = False
            invalid_count += 1

        try:
            if 0 <= height <= 1:
                pass
        except ValueError:
            print("invalid height")
            dataset_valid = False
            invalid_count += 1

print(f"invalid count:{invalid_count}")    

if dataset_valid:
    print("PASS")
else:
    print("FAIL")