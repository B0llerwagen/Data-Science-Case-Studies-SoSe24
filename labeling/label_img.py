import csv
import cv2
import os
import time
import random


def label_img(img_folder, csv_output):
    images = [img for img in os.listdir(img_folder) if img.endswith(".jpg")]
    random.shuffle(images)
    labels = []

    existing_labels = set()
    if os.path.exists(csv_output):
        with open(csv_output, mode='r', newline='') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)  # Skip header
            for row in reader:
                existing_labels.add(row[0])

    # Create the window for displaying the images outside the loop
    cv2.namedWindow("Image", cv2.WINDOW_AUTOSIZE)

    for i, img_name in enumerate(images):
        if img_name in existing_labels:
            print(f"Image {img_name} already labeled")
            continue

        img_path = os.path.join(img_folder, img_name)
        img = cv2.imread(img_path)
        if img is None:
            continue

        # Display the image in the already created window
        cv2.imshow("Image", img)
        cv2.waitKey(1)  # Necessary for the window to update
        time.sleep(0.2)

        print(f"Image nr:{i + 1}/{len(images)}, {img_name}")
        print("Press 'q' to quit and save")
        print("Press 'n' for useless image (no scooter)")
        print("Press 'y' to set all remaining rules as zero")
        print("Press 'Enter' to skip image")

        rules = [
            "Kein Scooter (0/1): ",
            "Scooter unvollständig/zu wenig Umgebung (0/1): ",
            "Scooter steht zu nah an Straße (Bordsteinkante) (0/1): ",
            "Scooter steht nicht frei (0/1): ",
            "Scooter auf Grünfläche (0/1): ",
            "Scooter blockiert Fahrradständer (0/1): ",
            "Scooter steht an ÖPNV Haltestelle / Parkverbot(0/1): ",
            "Scooter steht in Einfahrt / im Weg (0/1): "
        ]
        label = [img_name]
        for rule in rules:
            response = input(rule)
            if response == 'q':
                labels.append(label)
                break
            elif response == 'n':
                label.extend([1] * len(rules))
                break
            elif response == 'y':
                label.extend([0] * (len(rules) - len(label) + 1))
                break
            elif response == '':
                continue
            else:
                label.append(int(response))

        if response == 'q':
            break

        labels.append(label)

    cv2.destroyAllWindows()

    with open(csv_output, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(labels)

    print("Labeling completed and data saved")


label_img(os.path.join(os.path.dirname(__file__), ("../Yoio_Park_Proof")), "labels.csv")
