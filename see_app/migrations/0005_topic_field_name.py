# Generated by Django 3.1.1 on 2020-09-29 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('see_app', '0004_delete_imagetopic'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='field_name',
            field=models.ImageField(default='some pictures', upload_to=None),
        ),
    ]
