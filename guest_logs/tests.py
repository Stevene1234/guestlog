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

