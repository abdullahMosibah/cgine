# Generated by Django 3.1.7 on 2021-04-26 02:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lesson',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('time_added', models.DateField(auto_now_add=True)),
                ('title', models.CharField(default='new lesson', max_length=80)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('knowledge_block', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quiz', to='main.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='knowledge_block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('video', models.FileField(upload_to='videos/%y/%m/')),
                ('audio', models.FileField(null=True, upload_to='audios/%y/%m')),
                ('resource', models.TextField()),
                ('lesson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='knowledge_blocks', to='main.lesson')),
            ],
        ),
    ]
