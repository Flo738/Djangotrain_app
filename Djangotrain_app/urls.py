from django.contrib import admin
from django.urls import include, path



from . import views

urlpatterns = [
    path('index/', views.index,name="index"),
    path('show/<trains_id>', views.show,name="show"),
    path('hasard/', views.hasard, name='hasard'),
     path('recherche/', views.recherche, name='recherche'),

]
