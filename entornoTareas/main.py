#importamos httpexception para manejar errores
from fastapi import FastAPI, HTTPException
# importamos la libreria para permitir datos opcionales
from typing import Optional

# declaracion del objeto y la instaciamos de la clase FastAPI
app = FastAPI(
    title="Mi primer API 196",
    description="Domingo Araujo Alvarez",
    version="0.1"
)

#Creamos una lista para la base de datos 
tareas=[
    {"id":1, "nombre":"Tarea 1", "descripcion":"Descripcion de la tarea 1", "estado":"Pendiente"},
    {"id":2, "nombre":"Tarea 2", "descripcion":"Descripcion de la tarea 2", "estado":"Activo"},
    {"id":3, "nombre":"Tarea 3", "descripcion":"Descripcion de la tarea 3", "estado":"Pendiente"},
    {"id":4, "nombre":"Tarea 4", "descripcion":"Descripcion de la tarea 4", "estado":"Completada"},
    {"id":5, "nombre":"Tarea 5", "descripcion":"Descripcion de la tarea 5", "estado":"Activo"}
]


@app.get('/', tags=['Inicio'])
# metodo principal
def main():
    # retornamos en formato JSON un mensaje 
    return {'Hola Api Tareas':'Domingo Araujo'}

#Consultar Tareas
@app.get('/tareas', tags=['Tareas'])
def consultar_tareas():
    return tareas

#Consultar una tarea por su ID.
@app.get('/tareas/{id}', tags=['Tareas'])
def consultar_tarea(id: int):
    for t in tareas:
        if t['id'] == id:
            return t
    raise HTTPException(status_code=404, detail="Tarea no encontrada") 


#Agregar una nueva tarea.
@app.post('/tareas', tags=['Tareas'])
def agregar_tarea(tarea: dict):
    tarea['id'] = len(tareas) + 1
    tareas.append(tarea)
    return tarea
<<<<<<< Updated upstream
=======

#Actualizar una tarea existente.
@app.put('/tareas/{id}', tags=['Tareas'])
def actualizar_tarea(id: int, tarea: dict):
    for t in tareas:
        if t['id'] == id:
            t.update(tarea)
            return t
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

#Eliminar una tarea.
@app.delete('/tareas/{id}', tags=['Tareas'])
def eliminar_tarea(id: int):
    for t in tareas:
        if t['id'] == id:
            tareas.remove(t)
            return {"message": "Tarea eliminada correctamente"}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

>>>>>>> Stashed changes
