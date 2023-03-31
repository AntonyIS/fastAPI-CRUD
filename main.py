from typing import Union
import uuid
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates/")

app = FastAPI()
users = []

@app.get("/users")
def read_users(request: Request):
    return templates.TemplateResponse('home.html', context={'request': request,'users': users})


@app.post("/users")
async def post_users(request:Request):
    form = await request.form()
    email = form.get("email")
    password = form.get("password")
    user_id = str(uuid.uuid4())
    user = {"email": email, "password": password, "user_id": user_id}
    users.append(user)
    return templates.TemplateResponse('home.html', context={'request': request,'users': users})
    
@app.get("/users/{user_id}")
async def read_user(request:Request, user_id:str):
   
    for user in users:
       
        if user['user_id'] == user_id :
            
            return templates.TemplateResponse('user.html', context={'request': request,'user': user})
        else:
            return templates.TemplateResponse('user.html', context={'request': request,'user': {}})

@app.put("/users/{user_id}")
def update_user(user_id:int, q:Union[str, None] = None):
    return {
        "user" : f"user with id: {user_id}"
    }

@app.delete("/users/{user_id}")
def delete_user(user_id:int, q:Union[str, None] = None):
    return {
        "user" : f"user with id: {user_id}"
    }