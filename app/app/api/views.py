from drf_spectacular.utils import extend_schema_view, extend_schema

from rest_framework import viewsets

from api.serializers import TaskSerializer
from api.models import Task

#permite hacer cambios de esquema de openapi
@extend_schema_view(
    list= extend_schema(description='Permite obtener una lista de tareas'),
    retrieve = extend_schema(description='Permite obtener una tarea'),
    create = extend_schema(description='Permite crear una tarea'),
    update = extend_schema(description='Permite actualizar una tarea'),
    destroy = extend_schema(description='Permite eliminar una tarea'),   
)

#ViewSet es una clase de DRF para trabajar con los metodos CRUD
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
