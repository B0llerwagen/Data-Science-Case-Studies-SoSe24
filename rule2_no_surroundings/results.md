# Test results of model for rule 2
generally you want high recall on rare labels and high precision on labels that are more common
all *tested* on the same data

### MobileNetV2 architecture:
```
base_model.trainable = False

x = base_model.output
x = Conv2D(512, (3, 3), activation='relu')(x)
x = MaxPooling2D((2, 2))(x)
x = Normalization()(x)

x = Conv2D(512, (3, 3), activation='relu')(x)
x = MaxPooling2D((2, 2))(x)
x = Normalization()(x)
x = Flatten()(x)

x = Dense(512, activation='relu')(x)
x = Dropout(0.5)(x)
predictions = Dense(2, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)
```


pre_2_1 - trained with more data (more 0 in rule 2 (2x rule2 == 1))
          tested on 

                  precision    recall  f1-score   support

              0       0.86      1.00      0.92       281
              1       0.99      0.71      0.83       161

        accuracy                           0.89       442
       macro avg       0.92      0.85      0.87       442
    weighted avg       0.91      0.89      0.89       442
after trying to use this model it turns out it was rather bad but had the high accuracy due to a overlap of training / val data. With new data it performed much worse than the current best model (2_6.keras)

pre_2_2 - trained with less real data (1.5x rule2 == 1)

                  precision    recall  f1-score   support

              0       0.85      0.98      0.91       281
              1       0.94      0.71      0.81       161

        accuracy                           0.88       442
       macro avg       0.90      0.84      0.86       442
    weighted avg       0.89      0.88      0.87       442

pre_2_2 - trained with more real data and more (2200) images

                  precision    recall  f1-score   support

              0       0.81      0.98      0.88       281
              1       0.93      0.60      0.73       161

        accuracy                           0.84       442
       macro avg       0.87      0.79      0.81       442
    weighted avg       0.85      0.84      0.83       442


pre_2_3.keras - best weights - same data as 2_2 and 10 epochs

                  precision    recall  f1-score   support

              0       0.82      0.95      0.88       281
              1       0.89      0.63      0.73       161

        accuracy                           0.83       442
       macro avg       0.85      0.79      0.81       442
    weighted avg       0.84      0.83      0.83       442


pre_2_4 - result of 2_3.keras

                  precision    recall  f1-score   support

              0       0.79      0.99      0.88       281
              1       0.98      0.55      0.71       161

        accuracy                           0.83       442
       macro avg       0.89      0.77      0.79       442
    weighted avg       0.86      0.83      0.82       442

### MobileNetV2 other architecture:
```
base_model = keras.applications.MobileNetV2(input_shape=(512, 512, 3), include_top=False, weights='imagenet')

x = base_model.output

x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
x = Dropout(0.5)(x)

predictions = Dense(2, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)
```
seems to take way longer to calc

pre_2_5.keras - best weights new architecture

                  precision    recall  f1-score   support

              0       0.77      0.96      0.86       281
              1       0.89      0.51      0.65       161

        accuracy                           0.80       442
       macro avg       0.83      0.74      0.75       442
    weighted avg       0.82      0.80      0.78       442

pre_2_5 - result of 2_5.keras

                  precision    recall  f1-score   support

              0       0.70      0.99      0.82       281
              1       0.94      0.27      0.42       161

        accuracy                           0.73       442
       macro avg       0.82      0.63      0.62       442
    weighted avg       0.79      0.73      0.68       442



### EfficientNetB1 worked really bad and only guessed one option with multiple builds


### NASNetMobile with "best" MobileNetV2 architecture

pre_2_6.keras - best weights of new pre trained NASNetMobile

                  precision    recall  f1-score   support

              0       0.85      0.91      0.88       281
              1       0.82      0.71      0.76       161

        accuracy                           0.84       442
       macro avg       0.83      0.81      0.82       442
    weighted avg       0.84      0.84      0.84       442


pre_model_2_6.h5 - result of new pre trained NASNetMobile - same data as 2_2 5 epochs

                  precision    recall  f1-score   support

              0       0.84      0.90      0.87       281
              1       0.79      0.70      0.74       161

        accuracy                           0.82       442
       macro avg       0.82      0.80      0.80       442
    weighted avg       0.82      0.82      0.82       442



### InceptionV3 with "best" MobileNetV2 architecture

pre_2_6.keras - best weights of new pre trained InceptionV3

                  precision    recall  f1-score   support

              0       0.84      0.90      0.87       281
              1       0.80      0.71      0.75       161

        accuracy                           0.83       442
       macro avg       0.82      0.80      0.81       442
    weighted avg       0.83      0.83      0.83       442


pre_model_2_6.h5 - result of new pre trained InceptionV3 - same data as 2_2 5 epochs

                  precision    recall  f1-score   support

              0       0.83      0.93      0.87       281
              1       0.83      0.66      0.74       161

        accuracy                           0.83       442
       macro avg       0.83      0.79      0.80       442
    weighted avg       0.83      0.83      0.82       442