"""djangonized_api_rest/api/urls.py ."""
from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'usuarios', views.UserViewSet)
router.register(r'todos', views.ToDoViewSet)

urlpatterns = [
    url(r'^hola_mundo_rest/$', views.hola_mundo),
    url(r'^hola_mundo_rest/(?P<nombre>\w+)$', views.hola_mundo),
    # url(r'^usuarios/$', views.usuarios), APIView
    # url(r'^usuarios/$', views.user_list, name='usuarios'), ModelViewSet
    # url(r'^usuarios/(?P<id>\d+)$', views.usuarios, name='usuario'), APIView
    # url(r'^usuarios/(?P<id>\d+)$', views.user_detail, name='usuario'),
    url(r'^', include(router.urls)),
    # url(r'^todos/$', views.todos),
]
