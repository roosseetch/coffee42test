# -- coding: utf-8 --
import unittest

from django.test import TestCase
from django.db.models import get_model
from django.test.client import Client
from django.test.client import RequestFactory
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import auth

from .views import SirListView, RequestContetnView
from .forms import SirUpdateForm


Sir = get_model('chamber', 'Sir')
RequestContent = get_model('chamber', 'RequestContent')

# usersir = User(username="username", password="password", id=3)
usersir = User(id=3)


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

		Sir.objects.create(name='John', surname='Smith', date_birth='2000-10-10', created_by=usersir)
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

		Sir.objects.create(name='John', surname='Smith', date_birth='2000-10-10', created_by=usersir)
		response = SirListView.as_view()(request)
		self.assertEqual(response.context_data['object_list'].count(), 1)


class ChamberMiddlewareTests(TestCase):

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
		response = client.get(reverse('request'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, '<small>Requests Page</small></h1>')
		self.assertTemplateUsed(response, 'chamber/request.html')


class MemberContextProcessorsTests(TestCase):

	def test_if_settings_in_context(self):
		"""
		Tests if coffee42test.settings in context
		"""
		# factory = RequestFactory()
		# request = factory.get('/')

		# response = SirListView.as_view()(request)
		# self.assertEqual(response.context_data['coffee42test_settings'], settings)
		# self.assertIn('coffee42test_settings', response.context_data)

		client = Client()
		response = client.get(reverse('home'))
		self.assertEqual(response.context['coffee42test_settings'], settings)
		self.assertIn('coffee42test_settings', response.context)


class SirModelFormTests(unittest.TestCase):
	'''
	* Remember what Forms are for
	* Testing strategies
		- Initial states
		- Field Validation
		- Final state of cleaned_data
	'''
	def test_validation(self):
		form_data = {
			'name': 'Test Name',
			'surname': 'Test SurName',
			'bio': 'Test Name',
			'date_birth': '2000-10-10',
			'contact': 'Test Contact',
			# 'photo': '',
			# 'created_by': 3,
		}

		form = SirUpdateForm(data=form_data)
		self.assertTrue(form.is_valid())
		self.assertEqual(form.instance.name, 'Test Name')

		form.save()

		self.assertEqual(
			Sir.objects.get(id=form.instance.id).name,
			'Test Name'
		)


class SirFormEditTests(TestCase):
	fixtures = ['sir.json']

	def setUp(self):
		# Every test needs access to the request factory.
		self.factory = RequestFactory()

	def test_fixture_user(self):
		"""
		Testing if fixture user exist
		"""
		self.assertTrue(self.client.login(username='roosseetch', password='test'))

	def login_factory_test(self):
		# Create an instance of a GET request.
		request = self.factory.get(reverse('login'))

		# Test my_view() as if it were deployed at /customer/details
		response = auth.views.login(request)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, '<small>Login Page</small></h1>')
		self.assertTemplateUsed(response, 'chamber/login.html')


	def test_edit_login(self):
		self.client.logout()
		response = self.client.get(reverse('edit', kwargs={'pk': 1}))
		expected_url = reverse('login') + '?next=' + reverse('edit', kwargs={'pk': 1})
		self.assertRedirects(response, expected_url, target_status_code=200)
		response = self.client.post(reverse('login'), data={'username': 'roosseetch', 'password':'test'})
		self.assertEqual(response.status_code, 302)
		response = self.client.get(reverse('edit', kwargs={'pk': 1}))
		self.assertTemplateUsed(response, 'chamber/edit.html')
		self.assertContains(response, '<small>Edit Page</small></h1>')

	def test_edit_page(self):
		"""
		Tests that login url redirects properly and allow to log in
		"""
		# client = Client()
		self.client.login(username='roosseetch', password='test')
		response = self.client.get(reverse('edit', kwargs={'pk': 1}))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'chamber/edit.html')
		self.assertContains(response, '<small>Edit Page</small></h1>')
		self.assertIn('form', response.context)
		form = response.context['form']
		sir = Sir.objects.get(pk=1)
		self.assertEqual(sir, form.instance)

	# 	client.logout()
