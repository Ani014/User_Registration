from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm #to create a inbulit form using the UserCreationForm
    
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']





        
                                                                                                                           