from django.urls import path

from apps.modules.views import ModulesMainView

urlpatterns = [
    path('', ModulesMainView.as_view(), name='modules'),
]
