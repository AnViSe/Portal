from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    # path('', HomeView.as_view(), name='home'),
]
