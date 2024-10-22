from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from .forms import CollaborateRequestForm  # Import the specific form if testing it directly
from .views import collaborate_view  # Import the view if needed directly

class TestCollaborateView(TestCase):
    
    def test_collaborate_form_submission_success(self):
        response = self.client.post(reverse('collaborate'), {
            'name': 'Test Name',
            'email': 'test@example.com',
            'message': 'This is a test message.'
        })
        
        # Check the response redirection
        self.assertEqual(response.status_code, 302)  # Check for a redirect
        self.assertRedirects(response, reverse('collaborate_success'))  # Ensure it redirects to the success page
        
        # Check if the message was added
        messages_list = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages_list), 1)  # Ensure one message was added
        self.assertEqual(messages_list[0].tags, 'alert-success')  # Check if it’s a success message

    def test_collaborate_form_validation(self):
        # Test invalid form submission
        response = self.client.post(reverse('collaborate'), {
            'name': '',  # Empty name field
            'email': 'invalid-email',  # Invalid email
            'message': ''
        })
        
        # Expect to receive a 200 OK response as the form should fail validation
        self.assertEqual(response.status_code, 200)
        
        # Check that the form contains errors
        form = response.context['form']
        self.assertTrue(form.errors)

    def test_collaborate_success_page(self):
        # Test the success page rendering
        response = self.client.get(reverse('collaborate_success'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/collaborate_success.html')



    def test_successful_collaboration_request_submission(self):
       """Test for a user requesting a collaboration"""
       post_data = {
        'name': 'Test name',
        'email': 'test@email.com',
        'message': 'This is a test message'
    }
       response = self.client.post(reverse('collaborate'), post_data)  # Submit the form
       self.assertEqual(response.status_code, 302)  # Expecting a redirect on successful submission

    # Follow the redirect to check for the success message
       response = self.client.get(response.url)  # Follow the redirect
       self.assertIn(
          b'Collaboration request received! I endeavor to respond within 2 working days.', 
          response.content
    )

