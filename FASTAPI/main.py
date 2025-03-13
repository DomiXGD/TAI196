from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import Optional, List
from modelsPydantic import modelUsuario, modelAuth
from tokenGen import createToken
from Middlewares import BearerJWT


app = FastAPI(
    title="Mi primer API 196",
    description="Domingo Araujo Alvarez",
    version="0.1"
) 

usuarios = [
    {"id": 1, "nombre": "Jesús Cruz", "edad": 21, "correo":"jesuscruz@gmail.com"},
    {"id": 2, "nombre": "Estrella Cuellar", "edad": 20, "correo":"estrellacuellar@gmail.com"},
    {"id": 3, "nombre": "Lucero Cuellar", "edad": 20, "correo": "lucerocuellar@gmail.com"},
    {"id": 4, "nombre": "Domingo Ar aujo", "edad": 20, "correo": "domingoaraujo@gmail.com"},
]

@app.get("/", tags=["Inicio"])
def main():
    return {"Hola FastAPI": "Domingo Araujo Alvarez"}

#consultar todos los usuarios
@app.get("/usuarios",dependencies=[Depends(BearerJWT())], response_model= list[modelUsuario],tags=["Operaciones CRUD"])
def ConsultarTodos():
    return usuarios

#endpoint para generar un token 
@app.post('/auth',tags=['Autentificacion'])
def login(autorizado:modelAuth):
    if autorizado.correo == 'domi@example.com' and autorizado.passw == '123456789':
        token:str = createToken(autorizado.model_dump())
        print(token)
        return JSONResponse(content=token)
    else:
        return{"Aviso":"Usuario no autorizado"}

#endpoint para consultar un usuario por su id
@app.post("/usuarios/",response_model=modelUsuario,tags=["Operaciones CRUD"])
def AgregarUsuario(usuario: modelUsuario):  # Usa el modelo Usuario en lugar de dict
    for usr in usuarios:
        if usr["id"] == usuario.id:
            raise HTTPException(status_code=400, detail="El usuario ya existe")
    usuarios.append(usuario)
    return usuario
        
#Actualizar un usuario PUT
@app.put("/usuarios/{id}", response_model=modelUsuario,tags=["Operaciones CRUD"])
def ActualizarUsuario(id: int, usuarioActualizado:modelUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index]=usuarioActualizado.model_dump()
            return usuarios[index]
        
    raise HTTPException(status_code=400, detail="Usuario no encontrado")
        

@app.delete("/usuarios/{id}", tags=["Operaciones CRUD"])
def Eliminar(id: int):
    for usr in (usuarios):
        if usr["id"] == id:
            usuarios.remove(usr)
            return {"Usuario Eliminado": usr}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

    
