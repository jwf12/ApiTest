from django.urls import path
from .views import TareaList, TareaDelete

urlpatterns = [
    path('tarea/', TareaList.as_view()),
    path('tarea/<int:pk>', TareaDelete.as_view())
]