from django.urls import path
from relationship_app.views import display_books, DisplayLibraryView, SignUpView
from django.contrib.auth.views import LoginView
from .views.admin_view import admin_view
from .views.librarian_view import librarian_view
from .views.member_view import member_view
from . import views

urlpatterns = [
    path('books/', display_books, name='book-list'),
    path('library/<int:pk>/', DisplayLibraryView.as_view(), name='library-detail'),
    path('login/', LoginView.as_view(template_name='./templates/relationship_app/login.html'), name='login'),
    path('logout/', LoginView.as_view(template_name='./templates/relationship_app/logout.html'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
]
