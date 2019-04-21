"""djangonized_api_rest/api/serializers.py ."""
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from djangonized_api_rest.models import ToDo
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers

class UserSerializer(ModelSerializer):
    """class UserSerializer ."""

    class Meta:
        """class Meta of UserSerializer ."""

        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        write_only_fields = ('password',)


class ToDoSerializer(ModelSerializer):
    """class TodoSerializer ."""

    propietario = UserSerializer(User, many=False, )

    class Meta:
        """class Meta of TodoSerializer ."""

        model = ToDo
        fields = ('id', 'fecha_creado', 'fecha_finalizado', 'todo', 'hecho', 'propietario')
        read_only_fields = ('propietario',)


class ToDoHyperSerializer(HyperlinkedModelSerializer):
    """class TodoSerializer ."""

    propietario = serializers.HyperlinkedRelatedField(
        view_name='usuario',
        lookup_field='id',
        many=False,
        read_only=True,
    )

    class Meta:
        """class Meta of TodoSerializer ."""

        model = ToDo
        fields = ('id', 'fecha_creado', 'fecha_finalizado', 'todo', 'hecho', 'propietario')
