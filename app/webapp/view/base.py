from django.shortcuts import render

from webapp.models import Book


def index_view(request):
    records = Book.objects.filter(is_delete=False, status=Book.CHOICES[0][0]).order_by('created_at')
    context = {
        "records": records
    }
    return render(request, "index.html", context)
