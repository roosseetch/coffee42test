from django.views.generic import ListView
from django.db.models import get_model

Sir = get_model('chamber', 'Sir')
RequestContent = get_model('chamber', 'RequestContent')


class SirListView(ListView):
	model = Sir
	template_name = 'chamber/home.html'


class RequestContetnView(ListView):
	model = RequestContent
	queryset = RequestContent.objects.all().order_by('-date')[:10]
	template_name = 'chamber/request.html'
