from django.db import models

ESTADO_CHOICES = (
    ('ativo', 'Ativo'),
    ('inativo', 'Inativo'),
)

class Evento(models.Model):
    NIVEL_CHOICES = (
        ('basico', 'Básico'),
        ('medio', 'Médio'),
        ('avanc', 'Avançado'),
    )
    nome = models.CharField(max_length=255, null=False)
    estado = models.CharField(max_length=7,
                              choices=ESTADO_CHOICES,
                              default='ativo',
                              )
    nivel = models.CharField(max_length=6,
                             choices=NIVEL_CHOICES,
                             default='basico',
                             )
    tarefa = models.TextField(null=True)
    object = models.Manager()

    def __str__(self):
        return self.nome

class Check(models.Model):
    evento = models.ForeignKey(Evento,
                               on_delete=models.CASCADE,
                               related_name='Check_Evento',
                               null=True,
                               blank=True)
    datacriacao = models.DateTimeField(auto_now_add=True)
    dataatualizacao = models.DateTimeField(auto_now=True)
    observacao = models.CharField(max_length=255, null=True)
    estado = models.CharField(max_length=7,
                              choices=ESTADO_CHOICES,
                              default='ativo',
                              )
    object = models.Manager()

    def __int__(self):
        return self.evento

