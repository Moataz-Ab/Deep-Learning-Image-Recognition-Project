
import tensorflow as tf

def load_image_tensor(image_path):

    image_data = tf.io.read_file(image_path)
    # Decode the image data into a tensor
    image_tensor = tf.io.decode_image(image_data)
    return image_tensor

def load_image_from_file(file):
    image_data = file.read()
    image_tensor = tf.io.decode_image(image_data)
    return image_tensor
