from pydantic import BaseModel, Field, EmailStr


#modelo para validación de datos
class modelUsuario(BaseModel):
    id: int = Field(...,gt=0, description="Id unico y solo numeros positivos")
    nombre: str = Field(...,min_length=3 , max_length=215, description="Nombre solo debe de contener letras y espacios ")
    edad: int = Field(...,gt=0, lt=150, description="Edad solo numeros positivos")
    correo: str = Field(..., pattern="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$", description="Correo electronico valido",examples={"domi@gmail.com"})
    
class modelAuth(BaseModel):
    correo: EmailStr
    passw: str = Field(...,min_length=8,strip_whitespace=True, description="Contraseña minimo 8 caracteres")