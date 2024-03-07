from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
   path('', views.home, name='home'),
   path('Takeinput', views.Takeinput, name='Takeinput'),
   path('DeleteData<int:id>', views.DeleteData, name='DeleteData'),
   path('Update<int:id>', views.Update, name='Update'),
   path('EditData<int:id>', views.EditData, name='EditData'),
]
