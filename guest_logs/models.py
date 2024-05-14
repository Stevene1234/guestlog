from django.db import models


class Visit(models.Model):
    """Fields : name, visit_date, purpose, email(optional), phone(optional)"""
    name = models.CharField(max_length=100)
    visit_date = models.DateTimeField(auto_now_add=True)
    purpose = models.TextField()
    # email and name are optional.
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.visit_date}"
