from django.test import TestCase
from django.urls import reverse
from .models import About

class TestAboutView(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about_content = About.objects.create(
            title="About Me",
            content="This is about me."
        )

    def test_about_view_renders_correct_template(self):
        """Verifies that the about view uses the correct template"""
        response = self.client.get(reverse('about'))  # Make sure 'about' is the correct URL name
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')  # Check the template used

    def test_about_view_contains_correct_context(self):
        """Verifies that the context contains the correct about object"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('about', response.context)  # Ensure 'about' is in context
        self.assertEqual(response.context['about'], self.about_content)  # Ensure it matches the created content