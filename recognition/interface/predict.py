from recognition.interface.model import preprocess_input
from recognition.helpers.load_model import load_model
from recognition.interface.preprocessor import preprocess_image

def predict(image, model):
  
  X_processed = preprocess_image(image)
  y_pred = model.predict(X_processed)
  print("\n✅ prediction done: ", y_pred, "\n")
  return y_pred