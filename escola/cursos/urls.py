from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (
    CursoAPIView,
    AvaliacaoAPIView,
    CursosAPIView,
    AvaliacoesAPIView,
    CursoViewSet,
    AvaliacaoViewSet
)

router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)
urlpatterns = [
    path('curso/<int: pk>/', CursoAPIView.as_view(), name='curso'),
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int: curso_pk>/avaliacoes', AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),
    path('cursos/<int: curso_pk>/avaliacoes/<int: avalicao_pk>/', AvaliacaoAPIView.as_view(), name='curso_avaliacao'),
    path('avaliacao/<int: avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),

]