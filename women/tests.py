from django.test import TestCase
from http import HTTPStatus
from django.urls import reverse
from .models import Women



# Create your tests here.
class GetPagesTestCase(TestCase):
    fixtures = ['women_women.json', 'women_category.json', 'women_husbands.json', 'women_tagspost.json']
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

    def test_data_mainpage(self):
        w = Women.published.all().select_related('cat')
        path = reverse('home')
        response = self.client.get(path)
        self.assertQuerysetEqual(response.context_data['posts'], w[:5])

    def test_paginate_mainpage(self):
        path = reverse('home')
        page = 2
        paginate_by = 5
        response = self.client.get(path + f'?page={page}')
        w = Women.published.all().select_related('cat')
        self.assertQuerysetEqual(response.context_data['posts'], w[(page - 1) * paginate_by:page * paginate_by])

    def test_content_post(self):
        w = Women.published.get(pk=1)
        path = reverse('post', args=[w.slug])
        response = self.client.get(path)
        self.assertEqual(w.content, response.context_data['post'].content)
