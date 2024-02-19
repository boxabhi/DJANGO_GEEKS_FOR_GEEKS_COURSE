from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.views import View
import random
from home.forms import ContactForm
from home.models import Contact, Product
from django.contrib import messages
from .models import Student
from django.db.models import Sum, Avg, Min , Max, Count


def annotateStudents(search):
    students = Student.objects.annotate(num_skills = Count('skills')).filter(
        num_skills__gte = 1
        )
    if search:
        students = students.filter(name__icontains = search)
    return students


def index(request):
    search = request.GET.get('search')
    students = annotateStudents(search)
    student_age_sum = students.aggregate(Sum('age'))
    student_age_avg = students.aggregate(Avg('age'))
    student_age_max = students.aggregate(Max('age'))
    student_age_min= students.aggregate(Min('age'))


    context = {"students" : students, 
               'student_age_sum' : student_age_sum['age__sum'] ,
               'student_age_avg' : student_age_avg['age__avg'],
               'student_age_max' : student_age_max['age__max'],
               'student_age_min'  : student_age_min['age__min'],
               'search' : search
               }
    return render(request, 'index.html' , context)



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        Contact.objects.create(name = name)
        return redirect("/contact/")
    context = {'contacts' : Contact.objects.all()}
    return render(request, 'contact.html', context)

def delete_contact(request, id):
    contact = Contact.objects.get(id = id)
    contact.delete()
    return redirect("/contact/")




def about(request):
    return render(request, 'about.html')

# def contact(request):

#     if request.method == "POST":
#         form = ContactForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/contact/')


#     form = ContactForm()
#     context = {'form' : form}
#     return render(request, 'contact.html' , context)



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