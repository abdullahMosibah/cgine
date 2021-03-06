# Generated by Django 3.1.7 on 2021-06-09 14:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('icon', models.FileField(upload_to='category_icons/')),
            ],
        ),
        migrations.CreateModel(
            name='lesson',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('time_added', models.DateField(auto_now_add=True)),
                ('title', models.CharField(default='new lesson', max_length=80)),
                ('icon', models.FileField(null=True, upload_to='images/')),
                ('description', models.CharField(max_length=150)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='main.category')),
            ],
        ),
        migrations.CreateModel(
            name='knowledge_block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='new knowledge Block', max_length=100, null=True)),
                ('time_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('content', models.TextField()),
                ('video', models.FileField(upload_to='videos/')),
                ('audio', models.FileField(null=True, upload_to='audios/')),
                ('resource', models.TextField()),
                ('glossary', models.TextField(null=True)),
                ('lesson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='knowledge_blocks', to='main.lesson')),
            ],
        ),
    ]
