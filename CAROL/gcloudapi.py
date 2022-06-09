import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from fastapi import FastAPI

app = FastAPI()

# define a root `/` endpoint
@app.get("/predict")
def index():
    return {"ok": True}
