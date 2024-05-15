from django.test import TestCase
from .models import Visit
from django.utils import timezone


class VisitModelTest(TestCase):

    def setUp(self):
        self.visit = Visit.objects.create(
            name="John Doe",
            email="john.doe@example.com",
            phone="1234567890",
            visit_date=timezone.now(),
            purpose="Business Meeting"
        )

    def test_visit_creation(self):
        self.assertEqual(self.visit.name, "John Doe")
        self.assertEqual(self.visit.email, "john.doe@example.com")
        self.assertEqual(self.visit.phone, "1234567890")
        self.assertEqual(self.visit.purpose, "Business Meeting")
        self.assertTrue(isinstance(self.visit, Visit))
        self.assertEqual(str(self.visit), f"{self.visit.name} - {self.visit.visit_date}")

    def test_optional_fields(self):
        visit_without_email_and_phone = Visit.objects.create(
            name="Jane Doe",
            purpose="Consultation"
        )
        self.assertEqual(visit_without_email_and_phone.name, "Jane Doe")
        self.assertEqual(visit_without_email_and_phone.email, None)
        self.assertEqual(visit_without_email_and_phone.phone, None)
        self.assertEqual(visit_without_email_and_phone.purpose, "Consultation")
        self.assertTrue(isinstance(visit_without_email_and_phone, Visit))
        self.assertEqual(str(visit_without_email_and_phone), f"{visit_without_email_and_phone.name} - "
                                                             f"{visit_without_email_and_phone.visit_date}")



from django.urls import reverse
from .forms import VisitForm


class VisitSubmissionViewTest(TestCase):
    def test_get_request(self):
        """
        Test GET request to visit_submission view.
        """
        response = self.client.get(reverse('visit_submission'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'guest_logs/visit_submission.html')
        self.assertIsInstance(response.context['form'], VisitForm)

    def test_post_request_valid_data(self):
        """
        Test POST request with valid form data.
        """
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '1234567890',
            'purpose': 'Test purpose',
        }
        response = self.client.post(reverse('visit_submission'), data=form_data)
        self.assertEqual(response.status_code, 302)  # Redirects after successful submission

    def test_post_request_invalid_data(self):
        """
        Test POST request with invalid form data.
        """
        form_data = {}  # Invalid data with missing required fields
        response = self.client.post(reverse('visit_submission'), data=form_data)
        self.assertEqual(response.status_code, 200)  # Form submission fails, returns to the same page
        form = response.context['form']
        self.assertTrue(form.errors)  # Check if form has errors
        self.assertTrue('name' in form.errors)  # Check if 'name' field has error messages
        self.assertEqual(form.errors['name'], ['This field is required.'])  # Verify the specific error message

