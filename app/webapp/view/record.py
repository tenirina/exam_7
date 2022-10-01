from django.shortcuts import render, redirect
from django.urls import reverse

from webapp.forms import RecordForm
from webapp.models import Book


def errors_test(form):
    errors = {}
    if not form.data['name']:
        errors['name'] = 'Name should not be empty!'
    if not form.data['email']:
        errors['email'] = 'Email should not be empty!'
    if not form.data['text']:
        errors['text'] = 'Text should not be empty!'
    return errors


def create_view(request):
    form = RecordForm()
    if request.method == "GET":
        return render(request, 'add.html')
    form = RecordForm(request.POST)
    errors = errors_test(form)
    if errors:
        record = {
            'name': form.data['name'],
            'email': form.data['email'],
            'text': form.data['text']
        }
        return render(request, 'add.html', context={'record': record, 'errors': errors})
    if not form.is_valid():
        return render(request, 'add.html', context={'form': form})
    Book.objects.create(**form.cleaned_data)
    return redirect('index')


def update_view(request, pk):
    return render(request, 'add.html')
