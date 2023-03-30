# fastAPI-CRUD
A simple introduction to CRUD using FastAPI

# Technology stack
* FastAPI
* PostgreSQL

# Application structure
```.
├── config.py
├── controller.py
├── LICENSE
├── main.py
├── Makefile
├── model.py
├── README.md
├── requirements.txt
└── views.py
```

# Application installation
** Clone this code using the below command ** 
```git clone https://github.com/AntonyIS/fastAPI-CRUD.git```
** Navigate to the working directory ** 
```cd fastAPI-CRUD```
** Create virtual environment ** 
```python3 -m venv env```
** Activate virtual env ** 
```source env/bin/activate```
** Install dependancies e.i FastAPI and others ** 
```pip install fastapi```
```pip install "uvicorn[standard]" ```
** Run the API ** 
```make serve```