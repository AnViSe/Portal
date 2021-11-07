from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.modules.delivery.views import MailingView, MailingCreate

urlpatterns = [
    path('', login_required(MailingView.as_view()), name='mailings'),
    path('create/', login_required(MailingCreate.as_view()), name='add_mailing'),
    # path('<int:pk>/', login_required(AddressEdit.as_view()), name='edit_address'),
    # path('<int:pk>/view/', login_required(AddressView.as_view()), name='view_address'),
]
