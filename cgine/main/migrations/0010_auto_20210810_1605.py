# Generated by Django 3.1.7 on 2021-08-10 16:05

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210810_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knowledge_block',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]