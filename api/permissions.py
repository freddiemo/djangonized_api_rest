"""djangonized_api_rest/api/permissions.py ."""

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions
from djangonized_api_rest.models import ToDo

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS', ]


class HasAccessToToDos(permissions.BasePermission):
    """User has access to the requested ToDos ."""

    def has_permission(self, request, view):
        """Def has_permission of HasAccessToToDos ."""
        try:
            ToDo.objects.all()
        except ObjectDoesNotExist:
            return False

        print ('permission concedid')
        return True


class IsOwner(permissions.BasePermission):
    """User has access to the requested ToDos ."""

    def has_object_permission(self, request, view, obj):
        """Return True if the user is the owner of the object ."""
        if request.method in SAFE_METHODS:
            return True
        elif request.method == 'PUT' or request.method == 'PATCH' or request.method == 'POST' or request.method == 'DELETE':
            if obj.propietario == request.user:
                return True
            return False
