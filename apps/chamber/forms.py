# -- coding: utf-8 --
from django.forms import ModelForm
from django.db.models import get_model

Sir = get_model('chamber', 'Sir')


class SirForm(ModelForm):
	'''
	* ModelForms map a Model to a Form
	* Validation includes Model validators by default
	* Supports creating and editing instances
	* Key differences from Forms:
		- A field for the Primary Key (usually id)
		- .save() method
		- self.instance property
	'''

	class Meta:
		model = Sir
		# exclude = ('created_by',)
		# show all the fields!
		fields = ["name", "surname", "date_birth", "contact", "bio", "photo"]


class SirUpdateForm(ModelForm):
	'''
	Call the original __init__ method before assigning
	field overloads
	'''
	def __init__(self, *args, **kwargs):
		super(SirUpdateForm, self).__init__(*args, **kwargs)


	class Meta(SirForm.Meta):
		pass
