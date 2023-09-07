from tensorflow.keras.preprocessing import image
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras.applications.efficientnet import preprocess_input
# from tensorflow.keras.applications.efficientnet_v2 import preprocess_input
import numpy as np
import tensorflow as tf

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
    
# def preprocess_image(image):
#     img_array = np.array(image)
#     # resize image 
#     img_resized = tf.image.resize(img_array, (256, 256))
#     img_preprocessed = preprocess_input(img_resized) # preprcess
#     img_preprocessed = img_preprocessed[np.newaxis, ...] # add batch dimension
#     return img_preprocessed




def preprocess_image_tensor(image_tensor, target_size=(256, 256)):
    # Resize the image tensor to the target size
    img_resized = tf.image.resize(image_tensor, target_size)
    # Preprocess the image using the preprocess_input function
    img_preprocessed = preprocess_input(img_resized)
    # Expand the dimensions of the image from (height, width, channels) to (batch_size, height, width, channels)
    img_preprocessed = tf.expand_dims(img_preprocessed, axis=0)
    return img_preprocessed




