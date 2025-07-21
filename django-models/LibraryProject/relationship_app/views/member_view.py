from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from relationship_app.models import UserProfile

def is_member(user):
    try:
        return user.userprofile.role == 'MEMBER'
    except UserProfile.DoesNotExist:
        return False

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')