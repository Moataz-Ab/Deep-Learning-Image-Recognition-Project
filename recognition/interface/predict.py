from recognition.interface.model import preprocess, load_model
from recognition.interface.preprocessor import preprocess_image

def predict(image):
  model = load_model()
  assert model is not None
  
  X_processed = preprocess_image(image)
  y_pred = model.predict(X_processed)
  print("\n✅ prediction done: ", y_pred, "\n")
  return y_pred