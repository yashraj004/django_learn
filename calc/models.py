from django.db import models 
from django import forms

 # Create your models here.
class Post(models.Model):  
    name = models.CharField(max_length=20)  
    f_name  = models.CharField(max_length=30)
    class Meta:  
        db_table = "post"

class category(models.Model):  
    cat_name = models.CharField(max_length=20)  
    desc  = models.CharField(max_length=30)
    class Meta:  
        db_table = "category" 


class PostForm(forms.ModelForm):
    class Meta:
          model = Post 
          fields=['name','f_name']
          widgets = { 
            'name': forms.TextInput( attrs={ 'class': 'form-control', 'placeholder': 'Title', } )
            
                  }


