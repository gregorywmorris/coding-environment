# -*- coding: utf-8 -*-
"""
Created on 6/23/2024
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI, Request
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from BankNotes import BankNote
import pickle

# 2. Create the app object
app = FastAPI()

# Load the classifier
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# 3. Custom OpenAPI Schema
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Customized FastAPI",
        version="1.0.0",
        description='<img src="/static/images/swagger.png" alt="Swagger Image"/> \
            <p><strong>This is a customized FastAPI application with a personalized Swagger UI.</strong></p>',
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

'''
# 4. Custom OAuth2 Configuration (if needed)
oauth2_scheme = OAuth2Model(
    flows=OAuthFlowsModel(
        authorizationCode=OAuthFlowAuthorizationCode(
            authorizationUrl="https://example.com/oauth2/authorize",
            tokenUrl="https://example.com/oauth2/token",
            scopes={"read": "Read access", "write": "Write access"},
        )
    )
)
'''

# 5. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 6. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/Welcome?name=AnyNameHere
@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome To Krish Youtube Channel': f'{name}'}

# 7. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_banknote(data: BankNote):
    data = data.model_dump()
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    if prediction[0] > 0.5:
        prediction = "Fake note"
    else:
        prediction = "It's a Bank note"
    return {
        'prediction': prediction
    }

# 8. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# Command to run: uvicorn app:app --reload
