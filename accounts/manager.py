from django.contrib.auth.base_user import BaseUserManager



class Custommanager(BaseUserManager):

    def create_user(self , phone_number , password ,**extra_fields):
        if phone_number is None:
            raise ValueError("Phonenumber is required")
        user = self.model(phone_number = phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self , phone_number , password , **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)


        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must is_staff should be True")

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must is_staff should be True")
        
        if extra_fields.get('is_active') is not True:
            raise ValueError("Superuser must is_staff should be True")
        
        return self.create_user(phone_number, password , **extra_fields)