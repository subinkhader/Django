from django.urls import path,include
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('register', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('Addmedicine', views.addmedicine, name='addmedicine'),
    path('Listmedicine', views.listmedicine, name='listmedicine'),
    path('Viewmedicine/<int:id>', views.views, name='Viewmedicine'),
    path('Deletemedicine/<int:id>', views.delete, name='Deletemedicine'),
    path('Editmedicine/<int:id>', views.edit, name='Editmedicine'),
    
]
