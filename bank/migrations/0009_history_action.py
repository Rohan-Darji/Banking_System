# Generated by Django 3.2.7 on 2021-09-18 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0008_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='action',
            field=models.CharField(default='null', max_length=30),
        ),
    ]
