# Generated by Django 3.1.1 on 2020-10-20 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('see_app', '0010_auto_20201020_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='head',
            field=models.CharField(max_length=130, null=True, verbose_name='Заголовок'),
        ),
    ]
