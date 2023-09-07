from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras.applications.efficientnet_v2 import preprocess_input
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
def preprocess(directory):
    Xy = image_dataset_from_directory(
    directory= directory,
    labels='inferred',
    label_mode='categorical',
    class_names=None,
    color_mode='rgb',
    batch_size=32,
    image_size=(256, 256),
    shuffle=True,
    seed=None,
    validation_split=None,
    subset=None,
    interpolation='bilinear',
    follow_links=False,
    crop_to_aspect_ratio=False)
    
    Xy_preprocessed = Xy.map(lambda x, y: (preprocess_input(x), y))
    return Xy_preprocessed
    
def preprocess_image(image):
    img_array = np.array(image)
    # resize image 
    img_resized = tf.image.resize(img_array, (256, 256))
    img_preprocessed = preprocess_input(img_resized) # preprcess
    return img_preprocessed