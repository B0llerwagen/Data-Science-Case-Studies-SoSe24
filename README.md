TODO: resolve issue with model2 pre_trained not opening correctly 


# E-Scooter parking evaluation
This is a comprehensive guide to recreate and / or use our model to evaluate the parking situation of an e-scooter

# Requirements
Most importantly you need to have a folder with a lot of images of parked e-scooters names "Yoio_Park_Proof/" in the root directory.

Secondly you will need to operate in an virtual enviorment with a compatible version (everything works on [python 3.11.9](https://www.python.org/downloads/release/python-3119/)). Further you need to install all the requirements from the requirements.txt

This is all you need to get started.
If you already have the necessary CNNs for the final model you can skip to the Combining the CNNs in the final model part.

# Labeling the data
All the necessary files are in the labeling directory. Run [lable_img.py](./labeling/label_img.py) to start labeling data. 
You will see an Image and need to evaluate it on 8 different rules. 0 meaning the rule is NOT broken and the scooter is parked valid. 
There are some shortcuts to drastiacally decrease the time needed to label such as: 
- pressing y = perfectly parked scooter and everything is labeled as 0; 
- n = useless image aka an image that shows noting of / from the scooter, such as a black screen. 

After youre done labeling you **NEED to quit by pressing q**. This is the only way it saves all the new data properly. 

The data we used to create the CNNs is already saved in [labels.csv](labels.csv). By labeling, you´re just increasing the available data (aka appending to [labels.csv](labels.csv)). To create an completely new dataset just delete the file (this may be usefull if you need extremly accurate data as there are (probably) some mistakes in our labeled data).

# Creating the CNNs
After you gathered a sufficient amount of labeled data (or use the data we already gathered), you can start generating the CNNs.
For more infos on the specifics read [this](create_cnns/README.md).

# Combining the CNNs in the final model
To create the final model the all_models_combine folder is now of interest. To create / test your own model start by running the label_dataset file. 
There are 2 ways you can proceed. 
- using all models / rules: for this use the files with the "..._all 
- only use the most important rules / best model: use the "..._not_all_rules" files. They leave out some rules to increase accuracy (mostly due to bad model performance / bad data variety)

This can then be used in test_img_... to let all the CNNs predict your dataset. 
To evaluate it, use analyse_predictions_... to get the most important statistics of your predictions (like accuracy, recall etc.)

# Other
- [link](https://datashare.tu-dresden.de/s/JkNpycBKwpcJWXQ) to models if you dont want to generate them yourself
- make sure to save the models in a folder called models/ in the root directory
- the statistics of all the CNNs we used can be found [here](./all_models_combine/models_results.md)