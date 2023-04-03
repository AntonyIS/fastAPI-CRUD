from typing import Union# , Dict, List # > 3.8 
import uuid # Unique id 234eytrjhdgsadfsdavbsgnye, 10,000,000
from fastapi import FastAPI, Request # Form : UserForm : validation email must @ sign
from fastapi.templating import Jinja2Templates

"""
FastAPI : Create FastAPI application
Request : HTTP , GET, READ, PUT, DELETE, fetch from HTTP
Jinja2Templates : Used to pass python data to HTML, Data injection in HTML
    Render html pages
"""

# Define html directory: Dir for HTML pages
templates = Jinja2Templates(directory="templates/")

# app Application server
app = FastAPI()

# In memory database :PostgreSQL
users = []
# @-Decorator : 
# A decorator is a design pattern in Python that allows a user to add new functionality to an 
# existing object without modifying its structure. Decorators are usually called before the
# definition of a function you want to decorate.

# user = {"email" : "videl@gmail.com", "name": "Videl"}
# print(user["email"]) #videl@gmail.com
# print(user["name"]) #Videl

@app.get("/users")
def read_users(request: Request):    # templates/home.html
    return templates.TemplateResponse('home.html', context= {'request': request,'allUsers': users, "Dev": "VIDEL"})


@app.post("/users")
async def post_users(request:Request):
    # Access the form data using request.form()
    # async : parallel calls  at a time
    # sync : one call at a time
    form = await request.form()
    email:str = form.get("Myemail") 
    password:str = form.get("Mypassword") 
    user_id:str = str(uuid.uuid4()) 
    newUser = {"email": email, "password": password, "user_id": user_id} 
    users.append(newUser) # [] <== newUser
    # FastAPI CRUD APP using postgresql
    # https://betterprogramming.pub/my-first-crud-app-with-fast-api-74ac190d2dcc
    return templates.TemplateResponse('home.html', context={'request': request,'users': users})
    
# http://localhost:8000/users/12348 
@app.get("/users/{user_id}")
async def read_user(request:Request, user_id:str):
    users = [1,2,3,4,5,6,7]
    for user in users:
        if user['user_id'] == user_id :
            return templates.TemplateResponse('user.html', context={'request': request,'user': user})
        
    return templates.TemplateResponse('home.html', context={'request': request,'user': {}})

@app.put("/users/{user_id}")
async def update_user(user_id:int, request:Request):
    # Loop through existing users
            #0,     #1
    # users = ["jon", "mary"]
    for index, user in enumerate(users):
        if user['user_id'] == user_id :
            form = await request.form()
            email:str = form.get("Myemail") 
            password:str = form.get("Mypassword") 
            users[index][email]  = email
            users[index][password]  = password
            
            return templates.TemplateResponse('user.html', context={'request': request,'user': user})
    return {
        "user" : f"user with id: {user_id}"
    }

@app.delete("/users/{user_id}")
def delete_user(user_id:int):
    return {
        "user" : f"user with id: {user_id}"
    }