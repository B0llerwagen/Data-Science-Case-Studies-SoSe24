# Results 1 Model for all labels

rules:
          1  Kein Scooter
          2  Scooter unvollständig/zu wenig Umgebung
          3  Scooter steht zu nah an Straße (Bordsteinkante)
          4  Scooter steht nicht frei
          5  Scooter auf Grünfläche
          6  Scooter blockiert Fahrradständer
          7  Scooter steht an ÖPNV Haltestelle / Parkverbot
          8  Scooter steht in Einfahrt / im Weg

on new, more balanced data set
all_pre_2 is InceptionV3

*worse then .keras most likely due to overfitting*

all_pre_2.keras is InceptionV3 best weights

    Hamming Loss: 0.4779874213836478
    Accuracy: 0.5220125786163522
    Precision: [0.61788618 0.1        0.         0.         0.14285714 0.33333333    0.         0.        ]
    Recall: [0.86363636 0.04761905 0.         0.         0.09090909 0.25    0.         0.        ]
    F1 Score: [0.72037915 0.06451613 0.         0.         0.11111111 0.28571429    0.         0.        ]
    

all_pre_3 is mobilenetv2, 10epochs, all rules

    Hamming Loss: 0.3522012578616352
    Accuracy: 0.6477987421383647
    Precision: [0.67741935 0.5        1.         0.         1.         0.42857143    0.         0.        ]
    Recall: [0.95454545 0.19047619 0.66666667 0.         0.18181818 0.45    0.         0.        ]
    F1 Score: [0.79245283 0.27586207 0.8        0.         0.30769231 0.43902439    0.         0.        ]

all_pre_3.keras is mobilenetv2 best weights (with reduced epochs, without it was the same as full model)

    Hamming Loss: 0.41509433962264153
    Accuracy: 0.5849056603773585
    Precision: [0.63492063 0.4        0.         0.         0.         0.42105263    0.         0.25      ]
    Recall: [0.90909091 0.19047619 0.         0.         0.         0.4    0.         0.1       ]
    F1 Score: [0.74766355 0.25806452 0.         0.         0.         0.41025641    0.         0.14285714]



all_pre_4.h5 is NASNetMobile 10 epochs, all rules

    Hamming Loss: 0.5094339622641509
    Accuracy: 0.49056603773584906
    Precision: [0.65656566 0.15789474 0.         0.         0.66666667 0.26315789 0.         0.        ]
    Recall: [0.73863636 0.28571429 0.         0.         0.18181818 0.25 0.         0.        ]
    F1 Score: [0.69518717 0.20338983 0.         0.         0.28571429 0.25641026 0.         0.        ]


all_pre_4_1.h5 is NASNetMobile 20 epochs, all rules

    Hamming Loss: 0.4591194968553459
    Accuracy: 0.5408805031446541
    Precision: [0.67619048 0.22727273 1.         0.         0.2        0.30769231    0.         0.        ]
    Recall: [0.80681818 0.23809524 0.16666667 0.         0.09090909 0.4    0.         0.        ]
    F1 Score: [0.7357513  0.23255814 0.28571429 0.         0.125      0.34782609    0.         0.        ]


WITH CHOSEN LABELS

all_pre_chosen_5.keras

    Hamming Loss: 0.33962264150943394
    Accuracy: 0.660377358490566
    Precision: [0.71794872 0.33333333 0.6        0.52173913 1.        ]
    Recall: [0.89361702 0.19047619 0.27272727 0.54545455 0.18181818]
    F1 Score: [0.79620853 0.24242424 0.375      0.53333333 0.30769231]

  
all_pre_chosen_5.keras

    Hamming Loss: 0.37735849056603776
    Accuracy: 0.6226415094339622
    Precision: [0.69565217 0.30769231 0.375      0.5        0.66666667]
    Recall: [0.85106383 0.19047619 0.27272727 0.45454545 0.18181818]
    F1 Score: [0.76555024 0.23529412 0.31578947 0.47619048 0.28571429]


efficienctNetB3 -20 epochs
all_pre_chosen_6

    Hamming Loss: 0.33962264150943394
    Accuracy: 0.660377358490566
    Precision: [0.83146067 0.52631579 0.63636364 0.47826087 0.17647059]
    Recall: [0.78723404 0.47619048 0.63636364 0.5        0.27272727]
    F1 Score: [0.80874317 0.5        0.63636364 0.48888889 0.21428571]

all_pre_chosen_6.keras

    Hamming Loss: 0.27672955974842767
    Accuracy: 0.7232704402515723
    Precision: [0.80373832 0.57142857 0.8        0.5        0.66666667]
    Recall: [0.91489362 0.38095238 0.36363636 0.68181818 0.18181818]
    F1 Score: [0.85572139 0.45714286 0.5        0.57692308 0.28571429]

all_pre_chosen_7.keras with ResNet101V2

    Hamming Loss: 0.4591194968553459
    Accuracy: 0.5408805031446541
    Precision: [0.6754386  0.23076923 0.2        0.17647059 0.2       ]
    Recall: [0.81914894 0.14285714 0.18181818 0.13636364 0.09090909]
    F1 Score: [0.74038462 0.17647059 0.19047619 0.15384615 0.125     ]



new architecture;
```
base_model.trainable = False

x = base_model.output
x = Conv2D(512, (3, 3), activation='relu')(x)
x = MaxPooling2D((2, 2))(x)
x = Normalization()(x)

x = Conv2D(512, (3, 3), activation='relu')(x)
x = MaxPooling2D((2, 2))(x)
x = Normalization()(x)

x = GlobalAveragePooling2D()(x)
x = Normalization()(x)
x = Flatten()(x)

x = Dense(512, activation='relu')(x)
x = Dropout(0.5)(x)
predictions = Dense(5, activation='sigmoid')(x)

model = Model(inputs=base_model.input, outputs=predictions)

``` 

pre_8.keras 20epochs best weights

    Hamming Loss: 0.36477987421383645
    Accuracy: 0.6352201257861635
    Precision: [0.73394495 0.6        0.66666667 0.38461538 0.33333333]
    Recall: [0.85106383 0.14285714 0.18181818 0.68181818 0.09090909]
    F1 Score: [0.78817734 0.23076923 0.28571429 0.49180328 0.14285714]


pre_8.h5 20 epochs

    Hamming Loss: 0.3710691823899371
    Accuracy: 0.6289308176100629
    Precision: [0.70535714 0.33333333 0.57142857 0.48148148 0.25      ]
    Recall: [0.84042553 0.14285714 0.36363636 0.59090909 0.09090909]
    F1 Score: [0.76699029 0.2        0.44444444 0.53061224 0.13333333]

pre_9.keras 20 more epochs on top of pre_8.h5, best weights

    Hamming Loss: 0.4025157232704403
    Accuracy: 0.5974842767295597
    Precision: [0.72727273 0.25       0.6        0.41025641 0.25      ]
    Recall: [0.76595745 0.14285714 0.27272727 0.72727273 0.09090909]
    F1 Score: [0.74611399 0.18181818 0.375      0.52459016 0.13333333]

pre_9.h5 

    Hamming Loss: 0.3836477987421384
    Accuracy: 0.6163522012578616
    Precision: [0.73076923 0.125      0.5        0.45454545 0.25      ]
    Recall: [0.80851064 0.04761905 0.45454545 0.68181818 0.09090909]
    F1 Score: [0.76767677 0.06896552 0.47619048 0.54545455 0.13333333]