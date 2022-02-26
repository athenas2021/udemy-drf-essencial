from dataclasses import field
from rest_framework import serializers

from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kargs = {
            'email': {'write_only': True} # campo email não será apresentado nas requisições
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )

class CursoSerializer(serializers.ModelSerializer):
    # Nested Relationship
    avaliacoes =  AvaliacaoSerializer(many=True, read_only=True)

    # Hyperlinked Related Field
    # avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True,
    # view_name='avaliacao-detail')

    # Primary Key Related Field
    # avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )

''' 
Shell tests

from rest_framework.renderers import JSONRenderer
from cursos.models import Curso
from cursos.serializers import CursoSerializer
curso = Curso.objects.latest('id')
serializer = CursoSerializer(curso)
JSONRenderer().render(serializer.data)
'''