# Generated by Django 3.1.7 on 2021-08-10 06:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_lesson_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knowledge_block',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]