from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from django.contrib.auth.decorators import permission_required
from .models import Library, Book, Author

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

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author_id')
        author = get_object_or_404(Author, id=author_id)
        Book.objects.create(title=title, author=author)
        return redirect('book_list')
    authors = Author.objects.all()
    return render(request, 'relationship_app/add_book.html', {'authors': authors})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        author_id = request.POST.get('author_id')
        book.author = get_object_or_404(Author, id=author_id)
        book.save()
        return redirect('book_list')
    authors = Author.objects.all()
    return render(request, 'relationship_app/edit_book.html', {'book': book, 'authors': authors})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})