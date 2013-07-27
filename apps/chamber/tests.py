from django.test import TestCase
from django.db.models import get_model
from django.test.client import Client
from django.test.client import RequestFactory

from .views import SirListView


Sir = get_model('chamber', 'Sir')


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
