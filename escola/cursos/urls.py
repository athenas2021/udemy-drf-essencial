from django.urls import path
from .views import CursoAPIView, AvaliacaoAPIView, CursosAPIView, AvaliacoesAPIView

urlpatterns = [
    path('curso/<int: pk>/', CursoAPIView.as_view(), name='curso'),
    path('cursos/', CursoAPIView.as_view(), name='cursos'),
    path('avaliacao/<int: pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
    path('avaliacoes/', AvaliacaoAPIView.as_view(), name='avaliacoes'),

]