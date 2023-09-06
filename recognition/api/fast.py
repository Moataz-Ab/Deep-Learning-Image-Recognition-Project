from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

## model imports here

app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/predict")
def predict():

# preprocess

# predict with model

  return {
    "family": "family"
  }

@app.get("/")
def root():
  return {
    'api' '200'
  }