from keras import Model
def initialize_model(input_shape: tuple) -> Model:
  print("✅ Model initialized")
  return "model"

def compile_model():
  print("✅ Model compiled")
  return "model"
def train_model():
  
  print(f"✅ Model trained on {len(X)} rows with min val MAE: {round(np.min(history.history['val_mae']), 2)}")
  return "model, history"

def evaluate_model():

    print(f"✅ Model evaluated")
    return "metrics"
