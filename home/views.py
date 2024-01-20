from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import random




def index(request):
    lucky_number = random.randint(100 , 999)
    vegetables = ["Tomato 🍅" , "Potato 🥔" , "Chilly 🌶 ", "Carrot 🥕" , "Cucumber 🥒"]
    person_age = 15
    cities = [
    {"name": "Mumbai", "population": "19,000,000", "country": "India"},
    {"name": "New York", "population": "20,000,000", "country": "USA"},
    {"name": "Calcutta", "population": "15,000,000", "country": "India"},
    {"name": "Chicago", "population": "7,000,000", "country": "USA"},
    {"name": "Tokyo", "population": "33,000,000", "country": "Japan"},
]
    
    context = {"cities" : cities,"lucky_number" : lucky_number , "vegetables" : vegetables , "person_age" : person_age}
    return render(request, 'index.html' , context)


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def dynamic_url(request,id, name):
    print(f"This is the value that we got in the func -> {id}")
    return render(request, 'dynamic_url.html', context = {"id": id, "name" :name})



def project(request):
    lucky_number = random.randint(0 , 99)
    context = {"lucky_number" : lucky_number}
    return render(request ,"project/project.html" , context)