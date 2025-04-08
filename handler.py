from fastapi import FastAPI
import pickle

file = open('simple_model.pkl','rb')
model = pickle.load(file)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict/{input}")
@app.get("/predict/{input}")
def prediction_output(input: str):
    item_id = model.predict([[float(input)]])
    return {"prediction": float(item_id[0])}

# print(prediction_output('4.2'))