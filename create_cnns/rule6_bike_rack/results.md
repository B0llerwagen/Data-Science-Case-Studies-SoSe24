## All results are for rule 6
generally you want high recall on rare items and high precision on labels that are more common
all tested with the same data

pre_6_1:
base_model = MobileNetV2(input_shape=(512, 512, 3), include_top=False, weights='imagenet')

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

                        precision    recall  f1-score   support

                0       0.82      0.92      0.87        74
                1       0.87      0.73      0.79        55

    accuracy                                0.84       129
    macro avg           0.84      0.82      0.83       129
    weighted avg        0.84      0.84      0.83       129



pre_6_2:
base_model = MobileNetV2(input_shape=(512, 512, 3), include_top=False, weights='imagenet')

base_model.trainable = False

x = base_model.output
x = Conv2D(256, (3, 3), activation='relu')(x)
x = MaxPooling2D((2, 2))(x)
x = Normalization()(x)
x = Flatten()(x)

x = Dense(256, activation='relu')(x)
x = Dropout(0.3)(x)
predictions = Dense(2, activation='softmax')(x)

                    precision    recall  f1-score   support

                0       0.77      0.92      0.84        74
                1       0.85      0.64      0.73        55

    accuracy                                0.80       129
    macro avg           0.81      0.78      0.78       129
    weighted avg        0.81      0.80      0.79       129


pre_6_3:
base_model = MobileNetV2(input_shape=(512, 512, 3), include_top=False, weights='imagenet')

base_model.trainable = False

x = base_model.output
x = Conv2D(256, (5, 5), activation='relu')(x)
x = MaxPooling2D((2, 2))(x)
x = Normalization()(x)
x = Flatten()(x)

x = Dense(256, activation='relu')(x)
x = Dropout(0.3)(x)
predictions = Dense(2, activation='softmax')(x)

                precision    recall  f1-score   support

           0       0.70      0.84      0.77        74
           1       0.71      0.53      0.60        55

    accuracy                            0.71       129
    macro avg       0.71      0.68      0.68       129
    weighted avg    0.71      0.71      0.70       129


pre_6_4:
base_model = MobileNetV2(input_shape=(512, 512, 3), include_top=False, weights='imagenet')

base_model.trainable = False

x = base_model.output
x = Conv2D(512, (5, 5), activation='relu')(x)
x = MaxPooling2D((2, 2))(x)
x = Normalization()(x)
x = Flatten()(x)

x = Dense(512, activation='relu')(x)
x = Dropout(0.3)(x)
predictions = Dense(2, activation='softmax')(x)

                    precision    recall  f1-score   support

                0       0.85      0.72      0.78        74
                1       0.69      0.84      0.75        55

    accuracy                                0.77       129
    macro avg           0.77      0.78      0.77       129
    weighted avg        0.78      0.77      0.77       129

----------------------------------------------------------

pre_model_6_1_20_epochs.h5

base_model = MobileNetV2(input_shape=(512, 512, 3), include_top=False, weights='imagenet')

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

                        precision    recall  f1-score   support

                0       0.83      0.92      0.87        74
                1       0.87      0.75      0.80        55

    accuracy                                0.84       129
    macro avg           0.85      0.83      0.84       129
    weighted avg        0.85      0.84      0.84       129


----------------------------------------------------------


pre_model_6_1_40_epochs.h5

base_model = MobileNetV2(input_shape=(512, 512, 3), include_top=False, weights='imagenet')

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

                       precision    recall  f1-score   support

                    0       0.82      0.91      0.86        74
                    1       0.85      0.73      0.78        55

    accuracy                                    0.83       129
    macro avg               0.83      0.82      0.82       129
    weighted avg            0.83      0.83      0.83       129
