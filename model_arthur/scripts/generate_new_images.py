import os
from PIL import Image
import pandas as pd
from pandas import read_csv
import numpy as np
import tensorflow
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pickle

img_folder = "../Yoio_Park_Proof"
target_size = (512, 512)
label_data = read_csv("../balanced_labels.csv", sep=";")

# Function to load and resize an image
def load_image(img_path, target_size):
    with Image.open(img_path) as img:
        img = img.resize(target_size)
        img = img.convert('RGB')  # Ensure image is in RGB format
        return np.array(img)

# Read images and their corresponding labels
image_data = []
image_labels = []

for idx, row in label_data.iterrows():
    img_name = row['Image_name']
    img_path = os.path.join(img_folder, img_name)
    
    if os.path.exists(img_path):
        img_array = load_image(img_path, target_size)
        image_data.append(img_array)
        image_labels.append(row[1])  # Assuming labels are in columns after 'Image'
        print(f"Loaded image {img_name} with label {row[1]}", end='\r')
    else:
        print(f"Warning: Image {img_name} not found in folder {img_folder}")

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(image_data, image_labels, test_size=0.2, random_state=42)

X_train = np.array(X_train)
X_test = np.array(X_test)
y_train = np.array(y_train)
y_test = np.array(y_test)


import tensorflow
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pickle

datagen = ImageDataGenerator(
    rotation_range=20,
    vertical_flip=True,
    fill_mode='nearest'
)

#generate augmented images
batches = 100
augmented_images = []
augmented_labels = []

for i in range(batches):
    batch = next(datagen.flow(X_train, y_train, batch_size=1))
    augmented_images.append(batch[0][0])
    augmented_labels.append(batch[1][0])

    print(f"Generated {i+1} images", end='\r')