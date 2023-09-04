from django.urls import include, path
from . import views

urlpatterns = [
    path('resposta/', views.botAnswer, name='botAnswer')
]
