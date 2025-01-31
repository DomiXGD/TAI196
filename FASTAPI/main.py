from fastapi import FastAPI
from typing import Optional


app= FastAPI(
    title='Mi primer API 196',
    description='Domingo Araujo Alvarez',
    version='0.0.1'
) 

usuarios=[
    {"id":1, "nombre":"Domingo", "edad":21},
    {"id":2, "nombre":"Luis", "edad":22},
    {"id":3, "nombre":"Pedro", "edad":23},
    {"id":4, "nombre":"Juan", "edad":24},
]

@app.get('/', tags=['Inicio'])
def home():
    return {'hola FastAPI':'Domingo'}

#endPoint Parametro Obligatorio
@app.get('/Usuario/{id}',tags=['Parametro Obligatorio'])
def consultaUsuauio(id:int):
    #conectamosBD
    #hacemos consulta y regresamos resultados
    return{"Se encontro el usuario" : id}
    
@app.get('/promedio',tags=['Mi promedio TAI'])
def Promedio():
    return 9.7

#endPoint de Parametro Opcional
@app.get('/usuariox/', tags=['Parametro Opcional'])
def consultaUsuario2(id : Optional[int]= None):
    if id is not None:
        for usuario in usuarios:
            if usuario["id"]==id:
                return {"mensaje":"Usuario encontrado", "usuario":usuario}
        return {"mensaje":"Usuario no encontrado el id :{id}"}
    else:
        return {"mensaje":"No se proporciono el id"}
    
    
    


#endpoint con varios parametro opcionales
@app.get("/usuariosss/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}


