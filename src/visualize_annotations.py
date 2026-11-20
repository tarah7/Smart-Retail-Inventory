from pathlib import Path
import cv2
import matplotlib.pyplot as plt
datas=["train","valid","test"]
for data in datas:
    image_path=Path(f"data/dataset/{data}/images")

    images = list(image_path.glob("*.*"))

    for image in images:
        img = cv2.imread(str(image))

        if img is None:
            print(f"Invalid image: {image}")
            continue
        
        label_path= Path(f"data/dataset/{data}/labels/{image.stem}.txt")

        if not label_path.exists():
            print(f"there is no label image for {image}")
            continue

        content= label_path.read_text()
        lines= content.splitlines()
        for line in lines:
            values= line.split()

            if len(values) != 5:
                print("Invalid format")
                continue
            try:
                class_id = int(values[0])
                x_center=float(values[1])
                y_center=float(values[2])
                width = float(values[3])
                height = float(values[4])
            except ValueError:
                print("Non-numeric annotation")
                continue

            img_h,img_w=img.shape[:2]


            x_c= x_center * img_w
            y_c= y_center * img_h
            box_w= width * img_w
            box_h= height * img_h

            x1= int( x_c - (box_w/2))
            y1= int(y_c - (box_h/2))
            x2= int(x_c + (box_w/2))
            y2= int(y_c + (box_h/2))
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),1)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.show()