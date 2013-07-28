from django.test import TestCase
from django.db.models import get_model
from django.test.client import Client
from django.test.client import RequestFactory

from .views import SirListView, RequestContetnView


Sir = get_model('chamber', 'Sir')
RequestContent = get_model('chamber', 'RequestContent')


class SirModelTests(TestCase):
	"""
	Sir model tests.
	"""

	def test_str(self):
		sir = Sir(name='John', surname='Smith')
		self.assertEqual(str(sir), 'John Smith')

	def test_correct_template_render(self):
		"""
		Test that correct template rendered
		"""
		client = Client()
		response = client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, '<!DOCTYPE html>')
		self.assertTemplateUsed(response, 'chamber/home.html')


class SirListViewTests(TestCase):
	"""
	Sir list view tests.
	"""

	def test_sir_in_the_context(self):

		client = Client()
		response = client.get('/')

		self.assertEqual(list(response.context['object_list']), [])

		Sir.objects.create(name='John', surname='Smith', date_birth='2000-10-10')
		response = client.get('/')
		self.assertEqual(response.context['object_list'].count(), 1)

	def test_sir_in_the_context_request_factory(self):
		'''
		Test the same as in function test_sir_in_the_context, but instead of Client()
		using RequestFactory().
		Note that RequestFactory() tests faster then Client()
		'''

		factory = RequestFactory()
		request = factory.get('/')

		response = SirListView.as_view()(request)

		self.assertEqual(list(response.context_data['object_list']), [])

		Sir.objects.create(name='John', surname='Smith', date_birth='2000-10-10')
		response = SirListView.as_view()(request)
		self.assertEqual(response.context_data['object_list'].count(), 1)


class ChamberMiddlewareTest(TestCase):

	def test_request_data_collecting(self):
		'''
		Test if middleware fill database with requests
		'''
		client = Client()

		RequestContent.objects.all().delete()
		c = RequestContent.objects.all()
		self.assertEqual(len(c), 0)
		client.get('/')
		c = RequestContent.objects.all()
		self.assertTrue(len(c) > 0)
		self.assertEqual('/', c[0].path)
		self.assertEqual('GET', c[0].method)

	# Test doesn`t pass through
	def test_if_requests_10(self):
		"""
		Tests if 10 requests sent to template
		"""
		factory = RequestFactory()
		request = factory.get('/requests/')

		response = RequestContetnView.as_view()(request)

		self.assertEqual(list(response.context_data['object_list']), [])

		# Filling DBase with 15 requests
		[RequestContent(method=request.method, path=request.path,
			status_code=response.status_code).save() for i in range(15)]

		request = factory.get('/requests/')
		response = RequestContetnView.as_view()(request)
		self.assertEqual(response.context_data['object_list'].count(), 10)

	def test_request_link_redirects_properly(self):
		"""
		Tests if successful HTTP requests to needed page
		"""
		client = Client()
		response = client.get('/request/')
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, '<small>Requests Page</small></h1>')
		self.assertTemplateUsed(response, 'chamber/request.html')
