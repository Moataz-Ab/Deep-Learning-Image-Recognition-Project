#imports
from tensorflow.keras.utils import image_dataset_from_directory
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
from tensorflow.keras.callbacks import EarlyStopping

import tensorflow as tf
from tensorflow.keras.applications.efficientnet_v2 import EfficientNetV2B0
from tensorflow.keras.layers import Flatten, Dense, Dropout, Conv2D, MaxPooling2D
from tensorflow.keras.applications.efficientnet_v2 import preprocess_input
from keras import Model
from recognition.interface.preprocessor import preprocess

train_directory_url = "https://www.kaggle/input/split-balanced-classes/split_balanced_data/train"
val_directory_url = "https://www.kaggle/input/split-balanced-classes/split_balanced_data/validation"
test_directory_url = "https://www.kaggle/input/split-balanced-classes/split_balanced_data/test"

def initialize_model(input_shape: tuple) -> Model:
  print("✅ Model initialized")
  return "model"

def compile_model(model: Model, 
                  loss='categorical_crossentropy', 
                  optimizer='adam', 
                  metrics=['accuracy']):
      model.compile(loss=loss, optimizer=loss, metrics=metrics)
      print("✅ Model compiled")
      return model

def train_model(model: Model) -> Model:
    # preprcess
    Xy_val = preprocess(directory=val_directory_url)
    Xy_test = preprocess(directory=test_directory_url)
    Xy_train = preprocess(directory=train_directory_url)
    Xy_val_preprocessed = Xy_val.map(lambda x, y: (preprocess_input(x), y))
    Xy_train_preprocessed = Xy_train.map(lambda x, y: (preprocess_input(x), y))
    Xy_test_preprocessed = Xy_test.map(lambda x, y: (preprocess_input(x), y))

    early_stopping = EarlyStopping(
    monitor='val_loss',
    patience=5,
    restore_best_weights=True
    )

    history = model.fit(
    Xy_train_preprocessed,
    epochs=100,
    validation_data=Xy_val_preprocessed,
    verbose=1,
    callbacks=[early_stopping]
    )

    print(f"✅ Model trained on {len(X)} rows with min val MAE: {round(np.min(history.history['val_mae']), 2)}")
    return model, history

def evaluate_model(model: Model) -> Model:
    accuracy = model.evaluate(Xy_val_preprocessed, verbose=1)
    print(f"✅ Model evaluated")
    return accuracy

def base_model():
    base_model = EfficientNetV2B0(weights='imagenet', include_top=False, input_shape=(256, 256, 3))
    base_model.layer.trainable = False
    model = Sequential([
              base_model,
              Conv2D(128, (3, 3), activation='relu', padding='same'),
              MaxPooling2D((2, 2)),
              Conv2D(256, (3, 3), activation='relu', padding='same'),
              MaxPooling2D((2, 2)),
              Flatten(),
              Dense(256, activation='relu'),
              Dropout(0.5),
              Dense(128, activation='relu'),
              Dropout(0.5),
              Dense(9, activation='softmax')])
    print("✅Baseline Model initialized")
    return model

