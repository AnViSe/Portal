from django.urls import path, include
from rest_framework import routers

from apps.modules.delivery.views import MailingViewSet

router = routers.DefaultRouter()
# router = routers.SimpleRouter()

router.register(r'delivery', MailingViewSet)

urlpatterns = [
    path('', include(router.urls))
]
