from collections.abc import Iterable
from django.db import models

# Create your models here.


class College(models.Model):
    college_name = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.college_name
    

class Department(models.Model):
    department_name = models.CharField(max_length = 100)
    
    def __str__(self) -> str:
        return f" this is a department name {self.department_name}" 
    


class Skills(models.Model):
    skill_name = models.CharField(max_length = 100)



class Student(models.Model):
    student_id = models.CharField(max_length= 100 , null = True , blank = True)
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

    def save(self , *args , **kwargs):
        if not self.id :
            last_student_id = 1
            last_object = Student.objects.last()
            if last_object:
                last_student_id = last_object.id

            student_id = f"STU-{str(last_student_id).zfill(8)}"
            self.student_id = student_id
        else:
            self.update()

            
        super(Student, self).save(*args, **kwargs)


    def update(self , *args , **kwargs):
        print("UPDATE METHOD CALLED")

        



names = ['Rachel' , 'Aaron', 'Alexander', 'Daniel']

# student =Student.objects.filter(age__gte = 18 , age__lte = 20).exclude(name__icontains__in= names).order_by('name')

# YYYY-MM-DD


colleges = ['IIT Delhi', 'LPU' , 'AKTU', 'Baccha College']

departments = ['CS' , 'IT' , 'Mechanical', 'Civil']

skills  = ['Python' , 'English', 'Reading', 'Music']


