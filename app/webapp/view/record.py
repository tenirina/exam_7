from django.shortcuts import render, redirect
from django.urls import reverse

from webapp.forms import RecordForm
from webapp.models import Book


def create_view(request):
    form = RecordForm()
    if request.method == "GET":
        choices = Book.CHOICES
        return render(request, 'add.html', context={'choices': choices, 'form': form})
    form = RecordForm(request.POST)
    if not form.is_valid():
        return render(request, 'add.html', context={'choices': Book.CHOICES, 'form': form})
    record = Book.objects.create(**form.cleaned_data)
    return redirect(reverse('index'))


def update_view(request, pk):
    return render(request, 'add.html')
