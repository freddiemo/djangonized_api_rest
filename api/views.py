"""djangonized_api_rest/api/views.py ."""

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, ToDoSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from djangonized_api_rest.models import ToDo
from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework.filters import DjangoFilterBackend
from .filters import ToDoFilter
# Create your views here.


class HolaMundo(APIView):
    """class HolaMundo ."""

    def get(self, request, nombre, format=None):
        """Def save_model ToDo ."""
        return Response({'mensaje': 'Hi ' + nombre + 'World of DFR'})

hola_mundo = HolaMundo.as_view()


class Usuario(APIView):
    """Users ."""

    serializer_class = UserSerializer

    def get(self, request, id=None, format=None):
        """Def get of Usuario ."""
        if id is not None:
            users = get_object_or_404(User, pk=id)
            many = False
        else:
            users = User.objects.all()
            many = True
        response = self.serializer_class(users, many=many)
        return Response(response.data)

usuarios = Usuario.as_view()


class ToDoView(APIView):
    """ToDos ."""

    serializer_class = ToDoSerializer

    def get(self, request, id=None, format=None):
        """Def get of Usuario ."""
        todos = ToDo.objects.all()
        response = self.serializer_class(todos, many=True, )
        return Response(response.data)

    def post(self, request, format=None):
        """Def get of Usuario ."""
        todo = self.serializer_class(data=request.data)

        if todo.is_valid():
            todo.propietario = request.user
            todo.save()
            resp = self.serializer_class(todo, many=False)
            return Response(resp.data)
        else:
            return Response(todo.errors)

todos = ToDoView.as_view()


class UserViewSet(viewsets.ModelViewSet):
    """User ."""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'


class ToDoViewSet(viewsets.ModelViewSet):
    """To Do ."""

    # authentication_classes = (TokenAuthentication, SessionAuthentication)
    # permission_classes = (IsAuthenticated, HasAccessToToDos)
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
    lookup_field = 'id'
    permission_classes = (IsOwner, )
    filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('propietario', 'hecho',)
    filter_class = ToDoFilter

    def list(self, request, *args, **kwargs):
        """Def get of Usuario ."""
        print ('user request:', request.user)
        return super(ToDoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Def get of Usuario ."""
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.propietario = request.user
            self.pre_save(serializer, created=True)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED,
            headers=headers)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get_queryset(self):
        """Def get of Usuario ."""
        """print ('hello in queryset ')
        print ('kwargs:', self.kwargs)
        # queryset = self.queryset.filter(propietario=self.request.user)
        query = self.request.query_params
        print('query params:', query)
        queryset = self.queryset

        if 'username' in query.keys():
            queryset = queryset.filter(propietario=User.objects.get(username=query.get('username')))
        if 'hecho' in query.keys():
            done = True if query.get('hecho') == 'True' else False
            queryset = queryset.filter(hecho=done)

        return queryset"""

# user_list = UserViewSet.as_view({'get': 'list'})
# user_detail = UserViewSet.as_view({'get': 'retrieve'})
