from django.test import TestCase
from django.urls import reverse

class QueryToolTests(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_full_match(self):
        response = self.client.post(reverse('full_match'), {'text': 'Sample text', 'regex_querry': 'sample'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fullmatch.html')
        
    def test_first_match(self):
        response = self.client.post(reverse('first_match'), {'text': 'Sample text', 'regex_querry': 'sample'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'firstmatch.html')

