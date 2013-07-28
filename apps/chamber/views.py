from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.db.models import get_model

from .forms import SirUpdateForm

Sir = get_model('chamber', 'Sir')
RequestContent = get_model('chamber', 'RequestContent')


class SirListView(ListView):
	model = Sir
	template_name = 'chamber/home.html'


class RequestContetnView(ListView):
	model = RequestContent
	queryset = RequestContent.objects.all().order_by('-date')[:10]
	template_name = 'chamber/request.html'

class SirUpdateView(UpdateView):
	model = Sir
	form_class = SirUpdateForm
	template_name = 'chamber/edit.html'
	success_url = '/'
