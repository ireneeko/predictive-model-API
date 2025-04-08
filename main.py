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
def predict(input: str):
    item_id = model.predict([[float(input)]])
    return {"prediction": float(item_id[0])}

# print(predict('4.2'))