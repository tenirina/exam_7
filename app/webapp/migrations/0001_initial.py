# Generated by Django 4.1.1 on 2022-10-01 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('text', models.TextField(max_length=1000, verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date of update')),
                ('status', models.CharField(choices=[('active', 'Active'), ('blocked', 'Blocked')], default='active', max_length=50, verbose_name='Status')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Delete')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='Date of delete')),
            ],
        ),
    ]
