from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.views import View
import random
from home.forms import ContactForm
from home.models import Contact, Product
from django.contrib import messages




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

    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/contact/')


    form = ContactForm()
    context = {'form' : form}
    return render(request, 'contact.html' , context)



def checkEmptyorNot(value):
    return value is None or value is ''

def request_product(request):

    if request.method == "POST":
        product_name = request.POST.get('product_name')
        description = request.POST.get('remarks')
        quantity = request.POST.get('quantity')
        file = request.FILES['file']

        if checkEmptyorNot(product_name):
            messages.warning(request, "Product name cannot be null")
            return redirect('/request-product/')  

        if checkEmptyorNot(description):
            messages.warning(request, "description  cannot be null")
            return redirect('/request-product/')  


        if int(quantity) > 50 or int(quantity) <= 0:
            messages.warning(request, "Quantity cannot exceed more than 50 or less than 0")
            return redirect('/request-product/')
        
        if str(file).split('.')[1] != "pdf":
            messages.warning(request, "Only Pdf files are allowed")
            return redirect('/request-product/')
        

        product = Product.objects.create(
           product_name = product_name,
            description = description,
            quantity  = quantity,
            file = file ,
        )
        messages.success(request, "Product created.")
        return redirect('/request-product/')

    return render(request, 'request.html')

def dynamic_url(request,id, name):
    print(f"This is the value that we got in the func -> {id}")
    return render(request, 'dynamic_url.html', context = {"id": id, "name" :name})



def project(request):
    lucky_number = random.randint(0 , 99)
    context = {"lucky_number" : lucky_number}
    return render(request ,"project/project.html" , context)