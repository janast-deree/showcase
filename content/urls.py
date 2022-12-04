from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('filter_pieces', filter_pieces, name='filter_pieces'),
]