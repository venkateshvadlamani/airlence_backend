from rest_framework import serializers
from signup import models


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        author = serializers.ReadOnlyField(source='author.username')
        model = models.Signup
        fields = (
            'id',
            'author',
            'email',
            'message',
        )
