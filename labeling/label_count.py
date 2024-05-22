import csv

def label_count(csv_file):
  with open(csv_file, mode='r', newline='') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)  # Skip header
    labels = list(reader)
    
    rules = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for label in labels:
      #if all rules are 1, the image is useless
      if all([int(rule) == 1 for rule in label[1:]]):
        rules[8] += 1
        continue
      #if all rules are 0, the image is perfect
      if all([int(rule) == 0 for rule in label[1:]]):
        rules[9] += 1
        continue
      for i, rule in enumerate(label[1:]):
        rules[i] += int(rule)
        
    print(f"Rule 1: Kein Scooter (0/1): {rules[0]}")
    print(f"Rule 2: Scooter unvollständig/zu wenig Umgebung (0/1): {rules[1]}")
    print(f"Rule 3: Scooter steht zu nah an Straße (Bordsteinkante) (0/1): {rules[2]}")
    print(f"Rule 4: Scooter steht nicht frei (0/1): {rules[3]}")
    print(f"Rule 5: Scooter auf Grünfläche (0/1): {rules[4]}")
    print(f"Rule 6: Scooter blockiert Fahrradständer (0/1): {rules[5]}")
    print(f"Rule 7: Scooter steht an ÖPNV Haltestelle / Parkverbot(0/1): {rules[6]}")
    print(f"Rule 8: Scooter steht in Einfahrt / im Weg (0/1): {rules[7]}")
    
    print(f"Useless images: {rules[8]}")
    print(f"Perfect images: {rules[9]}")
    print(f"Total images: {len(labels)}")
    
label_count("labels.csv")