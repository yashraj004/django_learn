from django import forms

class PostForm(forms.ModelForm):
    class Meta:
       fields=['name','contact']




