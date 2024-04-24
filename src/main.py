from fastapi import FastAPI
import model
import utils

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello pussiosssss!!!!!!!!!!!!"}


@app.post("/predict", response_model = list[int])
async def predict(data: model.Data):
    results = utils.predict(data.model_dump())
    return results
