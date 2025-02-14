from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title="Mi primer API 196",
    description="Domingo Araujo Alvarez",
    version="0.1"
) 

usuarios = [
    {"id": 1, "nombre": "Jesús Cruz", "edad": 21},
    {"id": 2, "nombre": "Estrella Cuellar", "edad": 20},
    {"id": 3, "nombre": "Lucero Cuellar", "edad": 20},
    {"id": 4, "nombre": "Domingo Araujo", "edad": 20}
]

@app.get("/", tags=["Inicio"])
def main():
    return {"Hola FastAPI": "Domingo Araujo Alvarez"}

@app.get("/usuarios", tags=["Operaciones CRUD"])
def ConsultarTodos():
    return {"Todos los usuarios registrados": usuarios}

#endpoint para consultar un usuario por su id
@app.post("/usuarios/", tags=["Operaciones CRUD"])
def AgregarUsuario(usuario: dict):  # Usa el modelo Usuario en lugar de dict
    for usr in usuarios:
        if usr["id"] == usuario.get("id"):
            raise HTTPException(status_code=400, detail="El usuario ya existe")
    usuarios.append(usuario)
    return usuario
        

@app.put("/usuarios/{id}", tags=["Operaciones CRUD"])
def ActualizarUsuario(id: int, usuarioActualizado:dict):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index].update(usuarioActualizado)
            return usuarios[index]
    raise HTTPException(status_code=400, detail="Usuario no encontrado")
        

@app.delete("/usuarios/{id}", tags=["Operaciones CRUD"])
def Eliminar(id: int):
    for usr in (usuarios):
        if usr["id"] == id:
            usuarios.remove(usr)
            return {"Usuario Eliminado": usr}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

    
