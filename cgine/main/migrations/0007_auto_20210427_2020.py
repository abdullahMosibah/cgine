# Generated by Django 3.1.7 on 2021-04-27 20:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210427_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knowledge_block',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]