from django.shortcuts import render
from django.views.generic import DetailView
from models import Library

# Create your views here.
def display_books(request):
    return render(request, '../templates/list_books.html')

class DisplayLibraryView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library' 

class SignUpView():
    template_name = './templates/relationship_app/signup.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)