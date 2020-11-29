from django.db import models


# Create your models here.

class Topic(models.Model):
    """Посты, которые пишет пользователь."""
    head = models.CharField(max_length=130, null=True, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    date_added = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Созданно')

    class Meta:
        verbose_name_plural = 'Записи'
        verbose_name = 'Запись'
        ordering = ['-date_added']

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.text



