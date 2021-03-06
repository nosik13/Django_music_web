# Generated by Django 3.1.1 on 2020-10-20 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('see_app', '0009_topic_head'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'verbose_name': 'Запись', 'verbose_name_plural': 'Записи'},
        ),
        migrations.AlterField(
            model_name='topic',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Созданно'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='head',
            field=models.CharField(max_length=130, null=True, verbose_name='Загаловок'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
    ]
