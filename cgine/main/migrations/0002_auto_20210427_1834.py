# Generated by Django 3.1.7 on 2021-04-27 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knowledge_block',
            name='audio',
            field=models.FileField(null=True, upload_to='audios/'),
        ),
        migrations.AlterField(
            model_name='knowledge_block',
            name='video',
            field=models.FileField(upload_to='videos/'),
        ),
    ]