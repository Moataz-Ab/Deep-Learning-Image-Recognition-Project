## model imports here
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from recognition.interface.predict import predict, preprocess_image, load_model

app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
app.state.model = load_model(target="local") # load once

@app.get("/predict")
def predict():
  # image = load_image()
  # preprocess_image(image)

  return {
    "family": "family"
  }

@app.get("/")
def root():
  return {
    'api': '200'
  }