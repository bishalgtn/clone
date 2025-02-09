from django.shortcuts import render
from . import views
import requests

# # Create your views here.
# class homepage(views):
#     def get (self, request):
#         return render(request, "index.html")

def data():

    project_json_url = "https://api.github.com/users/Green-Software-Foundation/followers"

    response = requests.get(project_json_url)
    users = response.json()
    extracted_users = [{"name": user["login"], "profile_picture": user["avatar_url"], "views":user["id"]} for user in users]
    return extracted_users

def project(request):
    display_card = data()
    return render(request, "projects.html", {'display_data':display_card})