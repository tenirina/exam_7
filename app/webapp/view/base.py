from django.shortcuts import render

from webapp.forms import SearchForm
from webapp.models import Book


def index_view(request):
    form = SearchForm()
    form = SearchForm(request.GET)
    if 'search' in form.data:
        if form.data['search']:
            records = Book.objects.filter(name__icontains=form.data['search'], is_delete=False, status=Book.CHOICES[0][0]).order_by('created_at')[::-1]
        else:
            records = Book.objects.filter(is_delete=False, status=Book.CHOICES[0][0]).order_by('created_at')[::-1]
    else:
        records = Book.objects.filter(is_delete=False, status=Book.CHOICES[0][0]).order_by('created_at')[::-1]
    context = {
        "records": records
    }
    return render(request, "index.html", context)

