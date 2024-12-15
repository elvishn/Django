from django.test import TestCase
from http import HTTPStatus
from django.urls import reverse
# Create your tests here.
class GetPagesTestCase(TestCase):
    def test_mainpage_status_code(self):
        path = reverse('home')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
    def test_mainpage_template(self):
        path = reverse('home')
        response = self.client.get(path)
        self.assertTemplateUsed(response, 'women/index.html')

    def test_mainpage_title(self):
        path = reverse('home')
        response = self.client.get(path)
        self.assertEqual(response.context_data['title'], 'Главная страница')

    def test_redirect_addpage_redirect(self):
        path = reverse('add_page')
        redirect_uri = reverse('users:login') + '?next=' + path
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, redirect_uri)

