from django.urls import path
from . import views

urlpatterns=[
   
   path('',views.home),
   path('about',views.about),
   path('edit/int:id',views.edit),

]