from fastapi import FastAPI, File, UploadFile
from services.gcloud import detect_text
from services.farmacity import get_products
from utils.predictions import predict

app = FastAPI()

# define a root `/` endpoint
@app.get("/")
def index():
    return "Bienvenidos a CAROL Service API"

@app.post("/medicines")
def get_medicines(img_file: UploadFile = File(...)):
    list_of_words = detect_text(img_file.file)
    print("list_of_words" , list_of_words)
    predictions = predict(list_of_words)
    print("predictions", predictions)

    return get_products(predictions)
