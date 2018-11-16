# Generated by Django 2.1.3 on 2018-11-16 21:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('configpanel', '0002_configdev'),
    ]

    operations = [
        migrations.AddField(
            model_name='configdev',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='configdev',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
