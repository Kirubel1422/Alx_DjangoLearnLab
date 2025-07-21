from django.urls import path
from relationship_app.views import display_books, DisplayLibraryView, SignUpView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('books/', display_books, name='book-list'),
    path('library/<int:pk>/', DisplayLibraryView.as_view(), name='library-detail'),
    path('login/', LoginView.as_view(template_name='./templates/relationship_app/login.html'), name='login'),
    path('logout/', LoginView.as_view(template_name='./templates/relationship_app/logout.html'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
