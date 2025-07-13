## CREATE

```python
from myapp.models import Book book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

Output: <Book: 1984 by George Orwell (1949)>

## RETRIEVE

```python
book = Book.objects.get(title="1984") print(book.title, book.author, book.publication_year)
```

Output: 1984 George Orwell 1949

## UPDATE

```python
book.title = "Nineteen Eighty-Four" book.save()
```

Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>

## DELETE

```python
book.delete() books = Book.objects.all() print(list(books))
```

Output: []
