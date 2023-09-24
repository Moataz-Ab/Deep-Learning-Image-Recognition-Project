# Deep-Learning-Image-Recognition-Project

In this work, deep learning image recognition techniques are used to identify aircraft model types from aircraft images. 

![](Notebooks/prediction_example.jpeg)

## Dataset
The dataset is made available on Kaggle: https://www.kaggle.com/datasets/curiousstay/aircraft-dataset

The provided dataset consists of 3 subsets: 
- 1800 training images
- 900 validation images
- 900 testing images
Each subset consists of nine classes with balanced representation

## Key Requirements
- NumPy
- Pandas
- Tensorflow / Keras
- Matplotlib
- Seaborn
- Scikit-learn Metrics

## Approach:
- Training, validation, and testing sets are prepared using keras image_dataset_from_directory funtion
- Transfer learning model EfficientNetV2B1 is utilized
- The final model is optimized using techniques of augmentation, pooling, dropout, and regularization
- During model training, learning rate is adjusted using ReduceLROnPlateau callback
- Early stopping is introduced to prevent over fitting

## Summary of results
- Accuracy is chosed as the scoring metric
- The loss curve shows good learning pattern with no signs of overfitting
- The model shows good performance with 92% accuracy on both validation and test sets
- The accuracy of predicting individual classes varies in the range of 84-97%

## Presentation
You can watch the presentation of the project results here:
https://www.youtube.com/watch?v=IGT-SU5wNrg
