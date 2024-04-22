from django.test import TestCase
from django.urls import reverse


class TestUrls(TestCase):
    """Тесирование url ссылок"""
    def test_urls_archive(self):
        """Тестирование ссылки archive"""
        response = self.client.get(reverse('archive'))

        self.assertEqual(response.status_code, 200)

    def test_urls_CPU(self):
        """Тестирование ссылки cpu"""
        response = self.client.get(reverse('CPU'))

        self.assertEqual(response.status_code, 200)

    def test_urls_GPU(self):
        """Тестирование ссылки gpu"""
        response = self.client.get(reverse('GPU'))

        self.assertEqual(response.status_code, 200)
