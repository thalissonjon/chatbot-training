from django.urls import include, path
from . import views

urlpatterns = [
    path('chat/', views.conversation_test, name='chat')
]
