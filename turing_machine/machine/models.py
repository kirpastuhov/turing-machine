from django.db import models

class Data(models.Model):
	tape = models.CharField(max_length=1000)
	iteration = models.IntegerField()
	state = models.CharField(max_length=3)
	task = models.CharField(max_length=100)
	head_position = models.IntegerField(default=0)

class Step(models.Model):
	step = models.IntegerField(default=1)