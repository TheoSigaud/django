# Generated by Django 3.2.16 on 2022-11-14 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bibilio', '0003_auto_20221114_1114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='idAuthor',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='idEditor',
            new_name='editor',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='idGender',
            new_name='gender',
        ),
    ]
