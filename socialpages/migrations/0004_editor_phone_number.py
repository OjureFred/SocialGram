# Generated by Django 3.1 on 2020-08-08 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialpages', '0003_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='editor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]