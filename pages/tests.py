from django.test import TestCase
from django.urls import reverse

class PagesTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_about_page_template(self):
        response = self.client.get(reverse('aboutus'))
        # ✅ استفاده از نام دقیق قالبی که در views.py مشخص شده
        self.assertTemplateUsed(response, 'pages/about.html')
    
    def test_home_page_contains_correct_html(self):
        response = self.client.get(reverse('home'))
        # ✅ با توجه به محتوای home.html که 'home' است
        self.assertContains(response, 'home')