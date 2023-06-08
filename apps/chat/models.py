from django.db import models
from django.utils.translation import gettext_lazy as _


class Message(models.Model):
    text = models.TextField(
        _('Текст'),
        null=True,
        blank=True,
    )
    time = models.DateTimeField(
        _('Время'),
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.time}: {self.text}'

    class Meta:
        verbose_name = _('Сообщение')
        verbose_name_plural = _('Сообщения')
