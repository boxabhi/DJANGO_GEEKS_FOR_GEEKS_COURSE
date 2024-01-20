from collections.abc import Iterable
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

# DRY 

class BaseModel(models.Model):
    """Base class for all other models in the application."""
    this_field_is_from_basemodel =models.CharField(max_length=100 , default = "BASEMODEL")
    created_at = models.DateTimeField(auto_now = True)
    update_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        abstract = True



class ABC(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        app_label = "unqiue"


class College(BaseModel):
    college_name = models.CharField(max_length = 100)
    def __str__(self) -> str:
        return self.college_name
    

class Department(BaseModel):
    department_name = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now = True)
    update_at = models.DateTimeField(auto_now_add = True)
    def __str__(self) -> str:
        return f" this is a department name {self.department_name}" 
    


class Skills(BaseModel):
    skill_name = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now = True)
    update_at = models.DateTimeField(auto_now_add = True)

class Student(BaseModel):
    college = models.ForeignKey(College, on_delete= models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)
    name = models.CharField(max_length = 100)
    age = models.IntegerField(null = True, blank = True)
    gender = models.CharField(max_length=100, choices = (
        ("Male" , "Male"),
        ("Female", "Female")) , default="Male" )
    phone_number = models.CharField(max_length=10, null= True, blank=True)
    student_bio = models.TextField()
    email = models.EmailField()
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now = True)
    update_at = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['-name']
        



class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(blank = True)
    created_at = models.DateTimeField(auto_now = True)
    update_at = models.DateTimeField(auto_now_add = True)

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(f"{self.product_name}")
        super(Product, self).save(*args, **kwargs)


    class Meta:
        db_table = "product_table"
