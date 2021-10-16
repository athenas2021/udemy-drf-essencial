from enum import unique
from django.db import models


# Classe base abstrata
class Base(models.Model):
    # Data de criação, sempre será data atual (auto_now_add=True)
    criacao = models.DateTimeField(auto_now_add=True)
    # Data de atualização, sempre será data atual de update (auto_now=True) 
    atualizacao = models.DateTimeField(auto_now=True)
    # Status, sempre será verdadeiro por padrão
    ativo = models.BooleanField(default=True)

    # Definindo classe base abstrata, servirá de base para as outras classes
    class Meta:
        abstract = True


class Curso(Base):
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.titulo


class Avaliacao(Base):
    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2,decimal_places=1)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        # Cada e-mail pode avaliar uma única vez o curso
        unique_together = ['email','curso']

    def __str__(self):
        return f'{self.nome} avaliou o curso {self.curso} com nota {self.avaliacao}'