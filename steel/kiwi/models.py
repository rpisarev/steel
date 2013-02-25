from django.db import models

# Create your models here.
class Student(models.Model):
	fio = models.CharField(max_length = 255)
	birth = models.DateField()
	number = models.IntegerField()
	group = models.ForeignKey('Group', related_name = 'students')

	def __unicode__(self):
                return self.fio


class Group(models.Model):
	name = models.CharField(max_length = 255)
	starosta = models.ForeignKey(Student, related_name = '+')
	
	def __unicode__(self):
                return self.name

