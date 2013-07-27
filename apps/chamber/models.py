# -- coding: utf-8 --
from django.db import models


class Sir(models.Model):
	"""
	Dummy sir model used for testing
	"""
	name = models.CharField(
		'First name', max_length=50)
	surname = models.CharField(
		'Second name', max_length=50)
	bio = models.TextField('bio', max_length=1000)
	date_birth = models.DateField("Date of Birth")
	contact = models.TextField('contact', max_length=255)

	def __str__(self):
		return u"Person`s presentation {} {}".format(self.name, self.surname)
