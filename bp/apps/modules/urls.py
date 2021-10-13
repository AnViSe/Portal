from django.urls import path

from apps.modules.views import index

urlpatterns = [
    path('', index, name='modules'),
]
