from django.urls import path

from apps.modules.delivery.views import DeliveryMainView

urlpatterns = [
    path('', DeliveryMainView.as_view(), name='deliveries'),
]
