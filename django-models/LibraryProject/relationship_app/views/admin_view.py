from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from relationship_app.models import UserProfile

def is_admin(user):
    try:
        return user.userprofile.role == 'ADMIN'
    except UserProfile.DoesNotExist:
        return False

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')