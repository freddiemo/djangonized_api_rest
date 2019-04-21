"""djangonized_api_rest/models.py ."""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ToDo(models.Model):
    """class ToDo ."""

    fecha_creado = models.DateTimeField(auto_now=True)
    fecha_finalizado = models.DateTimeField()
    propietario = models.ForeignKey(User, related_name='propietario')
    todo = models.TextField()
    hecho = models.BooleanField(default=False)

    def __str__(self):
        """Def str ."""
        return u'{0} - {1}'.format(self.propietario, self.todo)

    def __unicode__(self):
        """Def unicode ."""
        return u'{0} - {1}'.format(self.propietario, self.todo)
