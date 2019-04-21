"""djangonized_api_rest/api/filters.py ."""
import django_filters
from djangonized_api_rest.models import ToDo


class ToDoFilter(django_filters.FilterSet):
    """Class ToDoFilter ."""

    username = django_filters.CharFilter(name='propietario__username')

    class Meta:
        """Clas Meta of ToDoFilter."""

        model = ToDo
        fields = ('hecho', 'propietario', 'username')
