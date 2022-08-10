from rest_framework.viewsets import ModelViewSet

from TODOapp.models import Project, Note
from TODOapp.serializers import ProjectModelSerializer, NoteModelSerializer
# Create your views here.

class ProjectModelViewSet(ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class NoteModelViewSet(ModelViewSet):

    queryset = Note.objects.all()
    serializer_class = NoteModelSerializer
