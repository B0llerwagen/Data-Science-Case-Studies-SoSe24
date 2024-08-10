models:
all on same labels


model1 = keras.models.load_model('../../models/pre_model_1_1_10_epochs.h5')
tested with more data (more 0 in rule 1 (2x rule1 == 1))

              precision    recall  f1-score   support

           0       0.90      1.00      0.95        47
           1       1.00      0.88      0.94        43

    accuracy                           0.94        90
   macro avg       0.95      0.94      0.94        90
weighted avg       0.95      0.94      0.94        90


model2 = keras.models.load_model('../../models/pre_model_2_6.keras')
trained/tested with more data (more 0 in rule 2 (2x rule2 == 1))

              precision    recall  f1-score   support

          0        0.84      0.90      0.87       281
          1        0.80      0.71      0.75       161

    accuracy                           0.83       442
   macro avg       0.82      0.80      0.81       442
weighted avg       0.83      0.83      0.83       442


model3 = keras.models.load_model('../../models/pre_model_3_1_10_epochs.h5')
tested with more(new) data (more 0 in rule 3 (2x rule3 == 1))

              precision    recall  f1-score   support

           0       0.64      0.84      0.73        44
           1       0.77      0.53      0.63        45

    accuracy                           0.69        89
   macro avg       0.71      0.69      0.68        89
weighted avg       0.71      0.69      0.68        89


model4 = keras.models.load_model('../../models/pre_model_4_1_10_epochs.h5')
tested with more(new) data (more 0 in rule 4 (2x rule4 == 1))

              precision    recall  f1-score   support

           0       0.85      0.94      0.89        18
           1       0.89      0.73      0.80        11

    accuracy                           0.86        29
   macro avg       0.87      0.84      0.85        29
weighted avg       0.86      0.86      0.86        29

saved before: 
              precision    recall  f1-score   support

           0       0.76      0.81      0.79        32
           1       0.77      0.71      0.74        28

    accuracy                           0.77        60
   macro avg       0.77      0.76      0.76        60
weighted avg       0.77      0.77      0.77        60


model5 = keras.models.load_model('../../models/pre_model_5_1_10_epochs.h5')
tested with more(new) data (more 0 in rule 5 (2x rule5 == 1))

              precision    recall  f1-score   support

           0       0.85      0.91      0.88        43
           1       0.87      0.79      0.83        34

    accuracy                           0.86        77
   macro avg       0.86      0.85      0.85        77
weighted avg       0.86      0.86      0.86        77





model6 = keras.models.load_model('../../models/pre_model_6_1_20_2_epochs.h5')

tested with more(new) data (more 0 in rule 6 (2x rule6 == 1))
              precision    recall  f1-score   support

           0       0.88      0.92      0.90       133
           1       0.85      0.78      0.81        73

    accuracy                           0.87       206
   macro avg       0.87      0.85      0.86       206
weighted avg       0.87      0.87      0.87       206


model7 = keras.models.load_model('../../models/pre_model_7_1_10_epochs.h5')

              precision    recall  f1-score   support

           0       0.93      0.93      0.93        15
           1       0.94      0.94      0.94        17

    accuracy                           0.94        32
   macro avg       0.94      0.94      0.94        32
weighted avg       0.94      0.94      0.94        32




model8 = keras.models.load_model('../../models/pre_model_8_1_10_epochs.h5')

              precision    recall  f1-score   support

           0       0.71      0.85      0.77        34
           1       0.75      0.56      0.64        27

    accuracy                           0.72        61
   macro avg       0.73      0.70      0.71        61
weighted avg       0.73      0.72      0.71        61