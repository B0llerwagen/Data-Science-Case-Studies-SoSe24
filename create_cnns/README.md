# How to create the CNNs
In this folder are several sub-folders. These each contain the necessary code to produce one of the CNNs used by us in the final model. This is a quick guide how to use them.


## For each of rule:
Each rule has 3 files which all serve a specific purpose. They are suppost to be run in the following order:
1. label_data_clean -> is used to create the necessary csv with the needed labels for the model
2. image_data_clean -> uses the previously created labels to load the corresponding images for the model
3. pre_trained -> uses the file created in image_data_clean to create and train a model for the respective rule

## Evaluating the CNNs:
After creating a model for a specific rule it can be evaluated in the same-named file evaluating.ipynb 
For this to work properly just adjust the file names for the specified rule. The comments in the file explain this in more detail.

## Modell for all rules
As part of our earlier testing we also created a model that would evaluate all rules at once. This got changed to a model that evaluated the 5 most important rules as the others were simply ignored by the former model. Even tho it has a worse performance then our final model it can also be generated. 
Located in the rule_all folder execute the files in this oder -> all_label_data_clean -> all_image_data_clean -> all_pre_clean. This should give you a working model. To evaluate it you need to use the all_evaluate file in the same folder. For a visual example how it works you can use test_model. 


####  Result-files
Some (rule 2 and 6) folders also have a result file. These were used in our early testing stages to track the model performance using different architectures. They were left in there for interested persons but are not needed to create and use the CNNs in any way shape or form.