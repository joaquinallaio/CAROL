from fastapi import FastAPI
from services.gcloud import detect_text
from services.farmacity import get_products
from utils.predictions import predict

app = FastAPI()

# define a root `/` endpoint
@app.get("/")
def index():
    return "Bienvenidos a CAROL Service API"

@app.get("/medicines")
def get_medicines(image):
    list_of_words = detect_text(image)
    predictions = predict(list_of_words)
    return get_products(predictions)
