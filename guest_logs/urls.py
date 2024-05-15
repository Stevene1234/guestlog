from django.urls import path
from .views import visit_submission

urlpatterns = [
    path('', visit_submission, name='visit_submission'),
]