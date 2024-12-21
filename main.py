from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

@app.get("/")
async def general() -> str:
    return "Главная страница"

@app.get("/user/admin")
async def admin() -> str:
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def id_call(user_id: Annotated[int, Path(ge=1,le=100, description="Enter User ID", examples=1)]) -> str:
    return f"Вы вошли как пользователь №{user_id}"

@app.get("/user")
async def user_call(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", examples="UrbanUser")]
                    , age: Annotated[int, Path(ge=18,le=120,description="Enter age", examples=24)]) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
