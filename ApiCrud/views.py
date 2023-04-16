from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import PassangerSerializer, RoomSerializer
from .models import Passanger, Room

# class TareaList(generics.ListAPIView):
#     serializer_class = TareaSerializer

#     def get_queryset(self):
#         queryset = Tarea.objects.all()
#         return queryset
    
# class TareaDelete(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = TareaSerializer
#     queryset = Tarea.objects.all()



# Passanger views.

class CreatePassenger(generics.ListCreateAPIView):
    serializer_class = PassangerSerializer

class ListPassanger(generics.ListAPIView):
    serializer_class = PassangerSerializer
    queryset = Passanger.objects.all()

class DeletePassanger(generics.RetrieveDestroyAPIView):
    serializer_class = PassangerSerializer
    queryset = Passanger.objects.all()

class UpdatePassenger(generics.RetrieveUpdateAPIView):
    serializer_class = PassangerSerializer
    queryset = Passanger.objects.all()


# Room views.

class CreateRoom(generics.ListCreateAPIView):
    serializer_class = RoomSerializer

class ListRoom(generics.ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class DeleteRoom(generics.RetrieveDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class UpdateRoom(generics.RetrieveUpdateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class RoomDirty(APIView):
    def post(self, request, pk):
        room = Room.objects.get(pk=pk)
        room.status = '#fffb8f'
        room.save()
        serializer = RoomSerializer(room)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class RoomClean(APIView):
    def post(self, request, pk):
        room = Room.objects.get(pk=pk)
        room.status = '#9bf0ac'
        room.save()
        serializer = RoomSerializer(room)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class OccuRoom(APIView):
    def post(self, request, pk):
        room = Room.objects.get(pk=pk)
        room.state = 2
        room.save()
        serializer = RoomSerializer(room)
        return Response(serializer.data, status=status.HTTP_200_OK)