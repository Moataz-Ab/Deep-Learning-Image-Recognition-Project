from tensorflow.keras.utils import image_dataset_from_directory

def preprocess(directory):
    return image_dataset_from_directory(
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
    
  