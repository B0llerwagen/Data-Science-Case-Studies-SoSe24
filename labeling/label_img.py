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

  for i, img_name in enumerate(images):
    if img_name in existing_labels:
      print(f"Image {img_name} already labled")
      continue
    
    img_path = os.path.join(img_folder, img_name)
    img = cv2.imread(img_path)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    time.sleep(0.2)
    
    print(f"Image nr:{i+1}/{len(images)}, {img_name}")
    print("Press 'q' to quit")
    print("Press 'n' for useless image (no scooter)")  
    print("Press 'y' for perfect image (scooter is parked perfectly)")
    print("Press 'Enter' to skip image")
    
    rule1 = input("Kein Scooter (0/1): ")
    if rule1 == 'q': break
    if rule1 == 'n':
        labels.append([img_name, 1, 1, 1, 1, 1, 1, 1, 1])
        continue
    if rule1 == 'y':
        labels.append([img_name, 0, 0, 0, 0, 0, 0, 0, 0])
        continue
    if rule1 == '': 
        continue
    rule2 = input("Scooter unvollständig/zu wenig Umgebung (0/1): ")
    rule3 = input("Scooter steht zu nah an Straße (Bordsteinkante) (0/1): ")
    rule4 = input("Scooter steht nicht frei (0/1): ")
    rule5 = input("Scooter auf Grünfläche (0/1): ")
    rule6 = input("Scooter blockiert Fahrradständer (0/1): ")
    rule7 = input("Scooter steht an ÖPNV Haltestelle / Parkverbot(0/1): ")
    rule8 = input("Scooter steht in Einfahrt / im Weg (0/1): ")    
    
    labels.append([img_name, rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8])
    cv2.destroyAllWindows()
            
            
  with open(csv_output, mode= 'a', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(labels)


label_img(os.path.join(os.path.dirname(__file__),("../Yoio_Park_Proof")), "labels.csv")
print("Labeling completed")   
