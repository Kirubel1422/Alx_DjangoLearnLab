from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from relationship_app.models import UserProfile

def is_librarian(user):
    try:
        return user.userprofile.role == 'LIBRARIAN'
    except UserProfile.DoesNotExist:
        return False

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')