from django.urls import path
from . import views

urlpatterns = [
    path('view-data/', views.view_data, name='view_data'),
]
