from django.urls import path
from app1 import views

# TEMPLATE TAGGING
app_name = 'app1'

urlpatterns = [
    path('index/',views.index, name = 'index'),
    path('application_form/', views.application_form, name='application_form'),
    #path('location/<int:title_id>', views.location, name='location'),
]