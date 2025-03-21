from pydantic import BaseModel, Field

class modelUsuario (BaseModel)
    codigoPostal: str = Field(...,min_length=5, description="solo numeros positivos")
    destino: str = Field(...,min_length=6, description="Solo debe de tener letras y espacios")
    peso: int = Field(...,gt=0,lt=500, description="Solo se permiten pesos de 1 a 500 gramos")
    
