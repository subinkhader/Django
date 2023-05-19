from django.urls import path,include
from . import views


urlpatterns = [
    path('apiregister', views.registration, name='apiregister'),
    path('apilogin', views.login, name='apilogin'),
    path('apilogout', views.logout, name='apilogout'),
    path('apiaddmedicine', views.addmedicine, name='apiaddmedicine'),
    path('apilistmedicine', views.listmedicine, name='apilistmedicine'),
    path('apiviewmedicine/<int:id>', views.viewmedicine, name='apiviewmedicine'),
    path('apidelete/<int:id>', views.delete, name='apidelete'),
    path('apiupdate/<int:id>', views.update, name='apiupdate'),
  
    
]
