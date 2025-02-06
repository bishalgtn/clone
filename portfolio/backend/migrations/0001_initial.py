# Generated by Django 5.1.6 on 2025-02-06 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('discription', models.CharField(max_length=3000, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('file_source_path', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
