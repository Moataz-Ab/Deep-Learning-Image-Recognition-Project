
from colorama import Fore, Style
from keras import Model
import glob
import os
from tensorflow import keras
from google.cloud import storage
from recognition.params import *

def load_model(stage="Production", target="local") -> Model:
      if target == "local":
        print(Fore.BLUE + f"\nLoad latest model from local storage..." + Style.RESET_ALL)
        # Get the latest model version name by the timestamp on disk
        # local_model_directory = os.path.join(LOCAL_PATH, "models")
        file_path = os.path.join(os.getcwd(), "models/model_optimized_92 acc.h5")
        # models_path = os.path.join(os.getcwd(), "models")
        local_model_paths = glob.glob(file_path)
        
        if not local_model_paths:
            print(Fore.RED + f"could not find path {file_path}" + Style.RESET_ALL)
            return None
        most_recent_model_path_on_disk = sorted(local_model_paths)[-1] #sorting models
        print(f"\nLoad latest model from ...{Fore.YELLOW}{local_model_paths[0]}" + Style.RESET_ALL)
        latest_model = keras.models.load_model(most_recent_model_path_on_disk)
        print(f"✅ Model {Fore.YELLOW}{os.path.basename(file_path)}{Style.RESET_ALL} loaded from local disk")
        return latest_model
      
      elif target == "gcs":
        print(Fore.BLUE + f"\nLoad latest model from GCS..." + Style.RESET_ALL)
        client = storage.Client()
        blobs = list(client.get_bucket(GCS_BUCKET).list_blobs(prefix="model"))

        try:
            latest_blob = max(blobs, key=lambda x: x.updated)
            print(f"📥 Downloading model: {latest_blob.name}") # latest model
            latest_model_path_to_save = os.path.join(LOCAL_PATH, latest_blob.name)
            latest_blob.download_to_filename(latest_model_path_to_save)
            latest_model = keras.models.load_model(latest_model_path_to_save)
            print("✅ Latest model downloaded from cloud storage")

            return latest_model
        except:
            print(f"\n❌ No model found in GCS bucket {BUCKET_NAME}")
            return None