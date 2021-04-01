from django.urls import path
from .views import *
app_name = 'home'

urlpatterns = [
    path('',HomeView.as_view(),name = 'home'),
    path('products/<slug>',ItemDetialView.as_view(),name = 'products'),
]