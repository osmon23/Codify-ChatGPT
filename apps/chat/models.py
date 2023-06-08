from django.db import models
from django.utils.translation import gettext_lazy as _


class Message(models.Model):
    question = models.TextField(
        _('Вопрос'),
        null=True,
        blank=True,
    )
    answer = models.TextField(
        _('Ответ'),
    )
    time = models.DateTimeField(
        _('Время'),
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.time}: {self.question} - {self.answer}'

    class Meta:
        verbose_name = _('Сообщение')
        verbose_name_plural = _('Сообщения')
