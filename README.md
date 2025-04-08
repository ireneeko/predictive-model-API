# predictive-model-API

This is a simple Python project that uses a pre-trained dummy model to return a numeric prediction based on one numeric input.

## Features

- **FastAPI Backend**: Exposes the predictive AI functionality as a RESTful API.
- **Live Deployment**: The API is deployed and accessible via a live URL on Render.
- **Postman for API Calls**: Use Postman to test and interact with the API.

## Requirements for local development

- Python 3.7+
- FastAPI
- Uvicorn
- scikit-learn
- numpy
- Postman (or other API testing application)

## Setup and Local Development

To run the app locally: 
1. Clone repository
```
https://github.com/ireneeko/predictive-model-API.git
```
2. Install the dependencies (terminal):
```
pip install -r requirements.txt
```
3. Use commented out print statement and replace value as desired
```
print(predict('4.2'))
```
4. Run the FastAPI app locally:
```
python .\main.py
```


## API Documentation

The API provides an endpoint to interact with the predictive AI model.

### 1. GET /

Basic Hello World

### 2. GET or POST /predict

This endpoint accepts a parameter input (float) and returns the prediction result.

**URL:** https://predictive-model-api.onrender.com/predict \
**Method:** `GET` or `POST`\
**Parameter:** `input`: The input value for prediction (float).

**Example Request** (using Postman):
```
GET https://predictive-model-api.onrender.com/predict/5.4
```
**Example Response:**
```
{"prediction":11.8}
```
Where `11.8` is the predicted result based on the input `5.4`.


## Live API on Render
API is live and hosted on Render. You can access it through the following URL:

**Live URL:** `https://predictive-model-api.onrender.com` 

Use this URL in your API requests (e.g., using Postman)

## Testing with Postman
1. Open Postman.
2. Create a new request:
     - **Method:** GET or POST (depending on which method you prefer to use)
     - **URL:** https://predictive-model-api.onrender.com/predict/{input}
       - replace {input} in URL with float value for input
3. Send the request.
4. View the response.

## Assumptions and Improvements

**Assumptions:**
- A basic understanding of Git and Python.
- Input is a numeric value


**Improvements:**
- Catch any improper input types so that the application does not break.
- Adding logging functionality to improve monitoring of the application's behavior.


