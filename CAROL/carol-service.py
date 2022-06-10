from fastapi import FastAPI, File, UploadFile
from services.gcloud import detect_text
from services.farmacity import get_products
from utils.predictions import predict
import shutil
from PIL import Image
import io

app = FastAPI()

# define a root `/` endpoint
@app.get("/")
def index():
    return "Bienvenidos a CAROL Service API"

#https://cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient
#
@app.post("/medicines")
def get_medicines(img_file: UploadFile = File(...)):
    list_of_words = detect_text(img_file.file)
    predictions = predict(list_of_words)
    return get_products(predictions)
