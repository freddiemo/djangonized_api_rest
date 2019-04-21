"""djangonized_api_rest/admin.py ."""
from django.contrib import admin
from .models import ToDo
# Register your models here.


class ToDoAdmin(admin.ModelAdmin):
    """class ToDo ."""

    list_display = ('propietario', 'todo', 'hecho')
    exclude = ('propietario')

    def save_model(self, request, obj, form, change):
        """Def save_model ToDo ."""
        obj.propietario = request.user
        obj.save()


admin.site.register(ToDo)
