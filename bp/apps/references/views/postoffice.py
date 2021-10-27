from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from apps.references.models.postoffice import PostOffice
from apps.references.serializers import PostOfficeSerializer


class PostOfficeViewSet(viewsets.ModelViewSet):
    """Список персон"""

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    queryset = PostOffice.objects.all()
    serializer_class = PostOfficeSerializer
