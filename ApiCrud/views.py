from rest_framework import generics
from .serializer import TareaSerializer
from .models import Tarea

class TareaList(generics.ListCreateAPIView):
    serializer_class = TareaSerializer

    def get_queryset(self):
        queryset = Tarea.objects.all()
        return queryset
    
class TareaDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TareaSerializer
    queryset = Tarea.objects.all()
