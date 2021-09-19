from django.urls import path, include

urlpatterns = [
    path('refs/', include('apps.references.urls_api')),
]
