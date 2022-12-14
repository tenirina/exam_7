
from django.db import models
from django.utils import timezone


class Book(models.Model):
    CHOICES = (
        ("active", "Active"),
        ("blocked", "Blocked")
    )

    name = models.CharField(verbose_name="Name", max_length=100, null=False, blank=False)
    email = models.EmailField(verbose_name="Email", null=False, blank=False)
    text = models.TextField(verbose_name="Text", max_length=1000, null=False, blank=False)
    created_at = models.DateTimeField(verbose_name="Date of creation", auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(verbose_name="Date of update", auto_now=True, null=True, blank=False)
    status = models.CharField(verbose_name="Status", null=False, max_length=50, choices=CHOICES, default=CHOICES[0][0])
    is_delete = models.BooleanField(verbose_name="Delete", default=False, null=False)
    deleted_at = models.DateTimeField(verbose_name="Date of delete", null=True, default=None)

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_delete = True
        self.save()
