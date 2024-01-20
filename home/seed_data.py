from .models import *
from faker import Faker
import random
fake = Faker()




def seedDB(num_records = 10):
    for record in range(0,num_records):
        college = College.objects.all().order_by('?')[0]
        department = Department.objects.all().order_by('?')[0]
        skills = Skills.objects.all().order_by('?')
        genders = ['Male' , 'Female']
        name = fake.name()
        age = random.randint(18 , 34)
        gender = random.choice(genders)
        phone_number = random.randint(100000000 , 9999999999)
        student_bio =  fake.sentence()
        email = fake.email()
        date_of_birth = fake.date()
        created_at = fake.date()
        student = Student.objects.create(
            college = college,
            department = department,
            name = name,
            age = age,
            gender = gender,
            phone_number = phone_number,
            student_bio = student_bio,
            email = email,
            date_of_birth = date_of_birth,
            update_at = created_at
        )
        for skill in skills[:2]:
            student.skills.add(skill)
            student.save()

        

