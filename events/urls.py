from django.urls import path
from .views import register, ParticipantList

urlpatterns = [
    path('', register, name='register'),
    path('list/', ParticipantList.as_view()),
]