from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    matricula = models.CharField(max_length=8)

    def __str__(self):
        return self.

    class class Meta:
        db_table = ''
        managed = True
        verbose_name_plural = 'Alunos'
        ordering = ['nome']

class Turma(models.Model):
    ano = models.IntegerField()
    semestre = models.TextChoices('1','2')

class Filiacao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    data_entrada = models.models.DateField(auto_now=True, auto_now_add=True)

"""
Os models a baixo são relativos ao jogo propriamente dito
"""

class Time(models.Model):
    nome_time = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_time
    
class Game(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    rank = models.IntegerField()
    serie = models.IntegerField()
    meta = models.FloatField()
    ambrosias = models.FloatField()



