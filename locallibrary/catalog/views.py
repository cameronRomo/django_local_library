from django.shortcuts import render
from django.views import generic
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
    # queryset = Book.objects.filter(title__icontains='the'[:3])
    template_name = 'books/book_list.html'

    def get_queryset(self):
        return Book.objects.filter(title__icontains='the'[:3])
    
    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context["some_data"] = "This is just some data"
        return context
    