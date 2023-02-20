from django.db import models


class FeedbackMessage(models.Model):
    fullname = models.CharField(verbose_name='Полное имя', max_length=255)
    phone = models.CharField(verbose_name='Номер телефона', max_length=16)
    email = models.EmailField(verbose_name='Адрес почты')
    message = models.TextField(verbose_name='Сообщение')
    agreement = models.BooleanField(verbose_name='Согласие на обработку ПД')
    date_send = models.DateTimeField(verbose_name='Дата отправления заявки', auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение/Вопрос'
        verbose_name_plural = 'Сообщения/Вопросы'

    def __str__(self):
        return self.fullname