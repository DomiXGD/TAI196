from fastapi import Examen2doP
from typing import Optional

app= Examen2doP(
    title="Examen 2do Parcial",
    description="Domingo Araujo Alvarez",
    version="0.1"
)

Envios=[
    {"Codigo Postal":"76720", "Destino":"El sauz", "Peso": 10},
    {"Codigo Postal":"12456", "Destino":"El marques", "Peso": 20},
    {"Codigo Postal":"21543", "Destino":"Pedro Escobedo", "Peso": 30},
    {"Codigo Postal":"76700", "Destino":"Ajuchitlan", "Peso": 40},
    {"Codigo Postal":"76234", "Destino":"Ignacio Perez", "Peso": 50},
]

@app.get('/Envios')
def get_Envios():
    return Envios

#endpoint para registrar 1 envio (muestre todos como resultado)
@app.post('/Envios')
def post_Envios(Codigo_Postal: str, Destino: str, Peso: int):
    Envios.append({"Codigo Postal": Codigo_Postal, "Destino": Destino, "Peso": Peso})
    return Envios

#endpoint para eliminar 1 envio por codigo postal
@app.delete('/Envios')
def delete_Envios(Codigo_Postal: str):
    for envio in Envios:
        if envio["Codigo Postal"]==Codigo_Postal:
            Envios.remove(envio)
            return Envios
    return {"Mensaje": "No se encontro el envio"}