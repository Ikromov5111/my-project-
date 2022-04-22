from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CreateUserForm(UserCreationForm):
    model = User
    fields = ['username','email', 'password1', 'password2']
    
class HotelForm(ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'
    
    
class WorkerForm(ModelForm):
    class Meta:
        model = Worker
        fields = '__all__'
    
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        
class RoomCreateForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        
class IjaraCreateForm(ModelForm):
    class Meta:
        model = Ijara
        fields = '__all__'
        