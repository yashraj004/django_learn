from django.shortcuts import render,redirect
from django.http import HttpResponse
from calc.models import Post,category, PostForm

# Create your views here.
def home(request):
    form= PostForm()
    data= Post.objects.all()
    if request.method == "POST":
      form=PostForm(request.POST)
      form.save()
      return redirect('/')
    return render(request, 'home.html', {'form' : form ,'result':data})

def edit(request, id):
    data= Post.objects.get(id= id)
    return render(request, 'edit.html', {'result':data})


    

def about(request):
    return HttpResponse ("about")