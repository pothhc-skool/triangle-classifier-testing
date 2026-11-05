from django.test import SimpleTestCase
from django.urls import reverse

from . import models
from .views import home


class HomeViewTests(SimpleTestCase):
    def test_home_page_returns_200_and_expected_content(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello, welcome to the home page!')

    def test_home_view_function_returns_expected_http_response(self):
        request = self.client.get('/').wsgi_request
        response = home(request)

        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello, welcome to the home page!', response.content.decode())


class ModelTests(SimpleTestCase):
    def test_models_module_is_importable(self):
        self.assertIsNotNone(models)
        self.assertTrue(hasattr(models, '__file__'))

# add tests for your views and models here


