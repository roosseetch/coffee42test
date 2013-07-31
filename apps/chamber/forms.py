# -- coding: utf-8 --
from django.forms import ModelForm
from django.db.models import get_model
from apps.chamber.widgets import DateWidget

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

		# show all the fields!
		# exclude = ('created_by',)
		fields = ["name", "surname", "date_birth", "contact", "bio", "photo"]

		dateTimeOptions = {
		'format': 'yyyy-mm-dd',
		'autoclose': 'true',
		'showMeridian' : 'false',
		'startDate' : '1950-1-1',
		'endDate' : '2014-1-1',
		'startView' : '4',
		'minView' : '2',
		}

		widgets = {
				'date_birth': DateWidget(attrs={'id':"calendar"}, options = dateTimeOptions)
			}


class SirUpdateForm(ModelForm):
	'''
	Call the original __init__ method before assigning
	field overloads
	'''
	def __init__(self, *args, **kwargs):
		super(SirUpdateForm, self).__init__(*args, **kwargs)


	class Meta(SirForm.Meta):
		pass
