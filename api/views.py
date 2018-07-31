from rest_framework import viewsets

from signup import models
from . import serializers


class SignupViewSet(viewsets.ModelViewSet):
    queryset = models.Signup.objects.all()
    serializer_class = serializers.SignupSerializer
