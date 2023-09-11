
from recognition.helpers.load_model import load_model
import numpy as np

aircraft_classes = ['737', '747', '767', 'A340', 'CRJ', 'DC', 'DHC', 'E', 'MD']
def predict_image(image_processed, model):
  y_pred = model.predict(image_processed)
  # y_pred_np = np.array(y_pred)
  predicted_index = np.argmax(y_pred)
  predicted_class = aircraft_classes[predicted_index]
  print("\n✅ predicted class: ", predicted_class, "✈️")
  print("✅ index: ", predicted_index, "\n")
  print("✅ probabilty: ", y_pred, "\n")
  return y_pred # probabilty np.array