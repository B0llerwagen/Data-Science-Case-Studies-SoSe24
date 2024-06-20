## All results are for rule 2
generally you want high recall on rare items and high precision on labels that are more common
all tested with the same data

pre_2_1 - trained with more data (more 0 in rule 2 (2x rule2 == 1))
          tested on 
              precision    recall  f1-score   support

           0       0.86      1.00      0.92       281
           1       0.99      0.71      0.83       161

    accuracy                           0.89       442
   macro avg       0.92      0.85      0.87       442
weighted avg       0.91      0.89      0.89       442


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