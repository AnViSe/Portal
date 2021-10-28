from django.urls import include, path

from apps.modules.views import ModulesMainView

urlpatterns = [
    path('', ModulesMainView.as_view(), name='modules'),
    path('delivery/', include('apps.modules.delivery.urls')),
]
