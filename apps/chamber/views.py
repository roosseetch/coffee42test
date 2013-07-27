from django.views.generic import ListView
from django.db.models import get_model

Sir = get_model('chamber', 'Sir')

class SirListView(ListView):
	model = Sir
	template_name = 'chamber/home.html'
