from django.shortcuts import render
from django.shortcuts import redirect
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import difflib
import os
from .models import *
# import json
# import random
# import torch
# from .model import NeuralNet
# from .nltk_utils import bag_of_words, tokenize
from pathlib import Path

# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#
BASE_DIR = Path(__file__).resolve().parent.parent


#
# with open(os.path.join(BASE_DIR, "CVT/intents.json"), 'r') as json_data:
#     intents = json.load(json_data)
#
# data = torch.load(os.path.join(BASE_DIR, "CVT/data.pth"))
#
# input_size = data["input_size"]
# hidden_size = data["hidden_size"]
# output_size = data["output_size"]
# all_words = data['all_words']
# tags = data['tags']
# model_state = data["model_state"]
#
# model = NeuralNet(input_size, hidden_size, output_size).to(device)
# model.load_state_dict(model_state)
# model.eval()
#

# Create your views here.
# def index(request):1.html")

# def login(request):
#     if 'username' in request.session:
#         return redirect(index)
#     if request.method == 'POST':
#         un = request.POST["username"]
#         pwd = request.POST["password"]
#         try:
#             obj = Users.objects.get(username=un)
#             if obj.password == pwd:
#                 request.session['username'] = un
#                 request.session['type'] = obj.type
#                 return redirect(index)
#             else:
#                 return render(request, "login.html", {"invalid_username": False, "invalid_password": True})
#         except Exception as e:
#             print(e)
#             return render(request, "login.html", {"invalid_username": True, "invalid_password": False})
#     return render(request, "login.html", {"invalid_username": False, "invalid_password": False})


def index(request):
    if 'username' in request.session:
        obj = Files.objects.all()
        s = set()
        l = set()
        for i in obj:
            s.add(i.company)
            l.add(i.version)
        return render(request, "index.html",
                      {"username": request.session['username'], "usertype": request.session['type'], "companies": s,
                       "versions": l})
    else:
        return redirect(login)


def logout(request):
    if 'username' in request.session:
        request.session.flush()

    return redirect(login)


def addupdate(request):
    if 'username' in request.session:
        try:
            obj = Files.objects.all()
            return render(request, "add-update.html", {"files": obj})
        except Exception as e:
            print(e)
            return HttpResponse("Sorry, some error please try again...!\nThe Error is: " + str(e))
    return redirect(login)


def addfile(request):
    if 'username' in request.session:
        try:
            obj = Files()
            obj.company = request.POST["company"]
            obj.version = request.POST["version"]
            obj.file = request.FILES["file"]
            obj.save()
            return redirect(addupdate)
        except Exception as e:
            print(e)
            return HttpResponse("Sorry, some error please try again...!\nThe Error is: " + str(e))

    return redirect(login)


def add(request):
    if 'username' in request.session:
        return render(request, "add.html")
    return redirect(login)


# def chat(request):
#     if 'username' in request.session:
#         return render(request,"chat.html")
#     return redirect(login)

def update(request):
    if 'username' in request.session:
        obj = Files.objects.get(id=request.GET["id"])
        return render(request, "update.html", {"company": obj.company, "version": obj.version, "file": obj.file})
    return redirect(login)


# @csrf_exempt
# def mresponse(request):
#     if 'username' in request.session:
#         sentence=request.POST["message"]
#         if request.session["type"]=='employee':
#             employee=True
#         else:
#             employee=False
#         sentence = tokenize(sentence)
#         X = bag_of_words(sentence, all_words)
#         X = X.reshape(1, X.shape[0])
#         X = torch.from_numpy(X).to(device)
#
#         output = model(X)
#         _, predicted = torch.max(output, dim=1)
#
#         tag = tags[predicted.item()]
#
#         probs = torch.softmax(output, dim=1)
#         prob = probs[0][predicted.item()]
#         if prob.item() > 0.75:
#             for intent in intents['intents']:
#                 if tag == intent["tag"]:
#                     if employee == True and ('private' in intent):
#                         return HttpResponse(random.choice(intent['private']))
#                     else:
#                         return HttpResponse(random.choice(intent['responses']))
#         else:
#             return HttpResponse("I do not understand...")


def uploadfile(request):
    if 'username' in request.session:
        try:
            obj = Uploadfile()
            obj.file = request.FILES["file"]
            obj.save()
            obj1 = Files.objects.get(company=request.POST['company'], version=request.POST['version'])

            with open(obj.file.name) as f1:
                f1_text = f1.read().split('\n')

            with open(obj1.file.name) as f2:
                f2_text = f2.read().split('\n')

            diff = difflib.HtmlDiff(wrapcolumn=75).make_file(f1_text, f2_text, obj.file.name[6:], f2.name)

            obj.delete()
            os.remove(obj.file.name)

            return HttpResponse(diff)

        except Exception as e:
            print(e)
            return HttpResponse("Sorry, some error please try again...!\nThe Error is: " + str(e))
    else:
        return redirect(login)

# def media(request):
#     if 'username' in request.session:
#         name=request.GET['fn']
#         redirect("../media/"+name)
#     return redirect(login)
