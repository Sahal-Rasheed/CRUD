from django.urls import path
from .views import *

urlpatterns = [
    path('register/',UserRegister.as_view(),name='register'),
    path('login/',UserLogin.as_view(),name='login'),
    path('logout/',UserLogout.as_view(),name='logout'),
    path('add/',AddStudent.as_view(),name='addstudent'),
    path('view/',StudentView.as_view(),name='studentview'),
    path('update/<int:id>',StudentUpdate.as_view(),name='studentupdate'),
    path('delete/<int:id>',StudentDelete.as_view(),name='studentdelete'),

    
]
