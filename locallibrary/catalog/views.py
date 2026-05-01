from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from .models import Book, Author, BookInstance, Genre

def index(request):
    """view function for home page of site"""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_genres = Genre.objects.count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # Books that contain the word 'All' in the title
    num_instances_all = BookInstance.objects.filter(book__title__contains='All').count()

    # The 'all()' is implied by default.abs
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances_all': num_instances_all,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_genres': num_genres,
        'num_authors': num_authors,
    }

    #render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    paginate_by  = 10

class AuthorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book
    
    def book_detail_view(self, request, primary_key):
        book = get_object_or_404(Book, pk=primary_key)
        return render(request, 'catalog/book_detail.html', context={'book': book})

class AuthorDetailView(generic.DetailView):
    model = Author

    def author_detail_view(self, request, primary_key):
        author = get_object_or_404(Author, pk=primary_key)
        return render(request, 'catalog/author_detail.html', context={'author: author'})