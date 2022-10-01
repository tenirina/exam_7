from django.contrib import admin

from webapp.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'text', 'status')
    list_filter = ('id', 'name', 'email', 'text', 'status')
    search_fields = ('name', 'email', 'text')
    fields = ('id', 'name', 'email', 'text', 'status')
    readonly_fields = ('id', 'name', 'email')


admin.site.register(Book, BookAdmin)
