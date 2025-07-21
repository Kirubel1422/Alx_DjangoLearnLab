import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings') 
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def main():
    try:
        author = Author.objects.get(name="Kassa") 
        books_by_author = Book.objects.filter(author=author)
        print(f"\nBooks by {author.name}:")
        for book in books_by_author:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print("Author not found.")

    try:
        library = Library.objects.get(name="Central Library") 
        books_in_library = library.book_set.all()
        print(f"\nBooks in {library.name}:")
        for book in books_in_library:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print("Library not found.")

    try:
        library = Library.objects.get(name="Central Library") 
        librarian = library.librarian 
        print(f"\nLibrarian of {library.name}: {librarian.name}")
    except (Library.DoesNotExist, Librarian.DoesNotExist, AttributeError):
        print("Librarian or Library not found.")

if __name__ == "__main__":
    main()
