from django.urls import path
from relationship_app.views import display_books, DisplayLibraryView

urlpatterns = [
    path('books/', display_books, name='book-list'),
    path('library/<int:pk>/', DisplayLibraryView.as_view(), name='library-detail'),
]
