from django.test import TestCase
from django.urls import reverse


class SignupPageTests(TestCase):

    def test_signup_page_status_code(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)

    def test_signup_template_used(self):
        response = self.client.get(reverse("signup"))
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_page_contains_form(self):
        response = self.client.get(reverse("signup"))
        self.assertContains(response, "<form")

    def test_signup_url_exists(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)