# Generated by Django 3.1.7 on 2021-06-20 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_membership_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.plan'),
        ),
    ]