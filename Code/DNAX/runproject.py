import os

url = "http://127.0.0.1:8000/PAT/login"

os.system("pip install django")
os.system("pip install openpyxl")

os.system("start chrome "+url)
os.system("python manage.py runserver")
