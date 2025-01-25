from fastapi import FastAPI


app= FastAPI()

@app.get('/')
def home():
    return {'hola FastAPI':'Domingo'}