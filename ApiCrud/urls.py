from django.urls import path
from .views import CreatePassenger, ListPassanger, DeletePassanger, UpdatePassenger, CreateRoom, ListRoom, DeleteRoom, UpdateRoom, RoomDirty, RoomClean, OccuRoom

urlpatterns = [
    #Passengers views:
    path('createP/', CreatePassenger.as_view(), name = 'create-passenger'),
    path('listP/', ListPassanger.as_view(), name='list-pass'),
    path('deleteP/<int:pk>', DeletePassanger.as_view(), name='delete-pass'),
    path('updateP/<int:pk>', UpdatePassenger.as_view(), name='update-pass'),

    #Room views:
    path('createR/', CreateRoom.as_view(), name = 'create-Room'),
    path('listR/', ListRoom.as_view(), name='list-Room'),
    path('deleteR/<int:pk>', DeleteRoom.as_view(), name='delete-Room'),
    path('updateR/<int:pk>', UpdateRoom.as_view(), name='update-Room'),
    path('dirtyR/<int:pk>', RoomDirty.as_view(), name='dirty-Room'),
    path('cleanR/<int:pk>', RoomClean.as_view(), name='clean-Room'),
    path('occuR/<int:pk>', OccuRoom.as_view(), name='occu-Room'),
]