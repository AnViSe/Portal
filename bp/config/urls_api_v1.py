from django.urls import path, include

urlpatterns = [
    path('refs/', include('references.urls_api')),
]
