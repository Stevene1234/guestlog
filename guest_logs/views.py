from django.shortcuts import render, redirect
from .forms import VisitForm


def visit_submission(request):
    """
    View to handle the visit submission form.
    """
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the same view to render a new, empty form
            return redirect('visit_submission')
    else:
        form = VisitForm()

    # If form is not valid, display error messages
    error_messages = form.errors.values() if form.errors else None

    return render(request, 'guest_logs/visit_submission.html', {'form': form, 'error_messages': error_messages})



