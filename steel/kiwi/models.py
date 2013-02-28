from django.db import models

# Create your models here.
class Student(models.Model):
	fio = models.CharField(max_length = 255)
	birth = models.DateField()
	number = models.IntegerField()
	group = models.ForeignKey('Group', related_name = 'students', null = True)

	def __unicode__(self):
                return self.fio


class Group(models.Model):
	name = models.CharField(max_length = 255)
	starosta = models.ForeignKey('Student', related_name = '+', null = True)

	def add_starosta(self, starosta):
		self.starosta = starosta
	
	def __unicode__(self):
                return self.name + ' ' + self.starosta.fio

