
from recognition.helpers.load_model import load_model
import numpy as np

aircraft_classes = ['737', '747', '767', 'A340', 'CRJ', 'DC', 'DHC', 'E', 'MD']
def predict_image(image_processed, model):
  y_pred = model.predict(image_processed)
  output = np.array(y_pred)
  predicted_index = np.argmax(output)
  predicted_class = aircraft_classes[predicted_index]
  print("\n✅ predicted class: ", predicted_class, "✈️")
  print("✅ index: ", predicted_index, "\n")
  return predicted_class