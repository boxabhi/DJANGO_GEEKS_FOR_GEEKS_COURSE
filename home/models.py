from collections.abc import Iterable
from django.db import models
from django.db.models.query import QuerySet
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


class StudentManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(is_deleted = False)

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
    is_deleted = models.BooleanField(default = False)

    objects = StudentManager()
    admin_objects = models.Manager()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['-name']
        



class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    description = models.TextField(null = True , blank = True)
    quantity = models.IntegerField()
    slug = models.SlugField(blank = True)
    created_at = models.DateTimeField(auto_now = True)
    update_at = models.DateTimeField(auto_now_add = True)
    file = models.FileField(upload_to="product/files")

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(f"{self.product_name}")
        super(Product, self).save(*args, **kwargs)


    class Meta:
        db_table = "product_table"


from django.db.models.signals import post_save , post_delete
from django.dispatch import receiver

class Contact(models.Model):
    name = models.CharField(max_length=100)
    contact_id = models.CharField(max_length = 100 , null=True , blank = True)


@receiver(post_save , sender = Contact)
def contact_obj_created(sender , instance, created , **kwargs):
    print("CONTACT CREATED")
    if created:
        instance.contact_id = f"{(instance.name)}-{str(instance.id).zfill(5)}"
        instance.save()


@receiver(post_delete , sender = Contact)
def contact_obj_deleted(sender , instance , **kwargs):
    print("CONTACT DELETDD")

