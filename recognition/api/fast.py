## model imports here
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from recognition.interface.predict import predict_image
from recognition.helpers.load_model import load_model
from recognition.helpers.load_image import load_image_tensor, load_image_from_file
from recognition.interface.preprocessor import preprocess_image_tensor

import os
from colorama import Fore, Style

app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
@app.on_event("startup")
async def startup_event():
    app.state.model = load_model(target="gcs") # load once

@app.post("/predict")
async def predict(file: UploadFile):
    if file.filename == '':
        return 'No selected file'
    if file:
        print(f"✔️ file received")
        image_tensor = load_image_from_file(file.file)
        image_processed = preprocess_image_tensor(image_tensor)
        class_name = predict_image(image_processed=image_processed, model=app.state.model)
        
    return {
        "predicted_class": f"{class_name}"
    }

@app.get("/predict")
def predict():
  image_path = os.path.join(os.getcwd(), "data/737_tarom.jpg")
  # print(Fore.YELLOW, f"{image_path}")
  image_tensor = load_image_tensor(image_path=image_path)
  # model=app.state.model
  image_processed = preprocess_image_tensor(image_tensor)
  class_name = predict_image(image_processed=image_processed, model=app.state.model)
  # class_name = model.predict(preprocess_image(image))
  return {
    "predicted_class": f"{class_name}"
  }

@app.get("/")
def root():
  return {
    'api': '200'
  }