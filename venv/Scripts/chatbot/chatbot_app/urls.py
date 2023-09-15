from django.urls import include, path
from . import views

urlpatterns = [
    path('chat/', views.botAnswer, name='chat')
]
