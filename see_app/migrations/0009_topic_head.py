# Generated by Django 3.1.1 on 2020-10-18 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('see_app', '0008_remove_topic_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='head',
            field=models.CharField(max_length=130, null=True),
        ),
    ]
