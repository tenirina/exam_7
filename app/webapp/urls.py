from django.urls import path

from webapp.view.base import index_view
from webapp.view.record import create_view, update_view, delete_view, confirm_delete_view

urlpatterns = [
    path("", index_view, name='index'),
    path("create/", create_view, name="create"),
    path("update/<int:pk>", update_view, name="update"),
    path("delete/<int:pk>", delete_view, name='delete'),
    path("confirm-delete/<int:pk>", confirm_delete_view, name='confirm_delete')
]
