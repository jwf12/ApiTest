from rest_framework import serializers
from .models import Passanger, Room

# class TareaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tarea
#         fields = ('__all__')


class PassangerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passanger
        fields = ('__all__')


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('__all__')