# -- coding: utf-8 --
from django.conf import settings
from django.db import models

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Sir(models.Model):
	"""
	Dummy sir model
	"""
	name = models.CharField(
		'First name', max_length=50)
	surname = models.CharField(
		'Second name', max_length=50)
	bio = models.TextField('bio', max_length=1000)
	date_birth = models.DateField("Date of Birth")
	contact = models.TextField('contact', max_length=255)
	photo = models.ImageField(upload_to='photo', blank=True)
	created_by = models.ForeignKey(AUTH_USER_MODEL)

	def __str__(self):
		return ' '.join([self.name, self.surname])


class RequestContent(models.Model):
	'''
	REST APIs rely on HTTP method for each type of action:
	Create a new resource									POST
	Read an existing resource								GET
	Request the header of an existing resource				HEAD
	Update an existing resource								PUT
	Update part of an existing resource						PATCH
	Delete an existing resource								DELETE
	Return the supported HTTP methods for the given URL		OPTIONS
	Echo back the request									TRACE
	Tunneling over TCP/IP (usually not implemented)			CONNECT
	'''
	method = models.CharField(max_length=7)
	path = models.TextField('Path', max_length=255)
	date = models.DateTimeField( auto_now_add=True)
	status_code = models.IntegerField('Status code', max_length=3)

	def __str__(self):
		return ' '.join([self.path, self.status_code])
