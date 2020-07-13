from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=1000, verbose_name='название опроса', blank=False, default='')
    description = models.TextField(verbose_name='описание', blank=True, null=True)
    start_pub = models.DateField(auto_now=False, auto_now_add=False)
    end_pub = models.DateField(auto_now_add=False, auto_now=False)

    class Meta:
        verbose_name = 'опрос'
        verbose_name_plural = 'опросы'
        ordering = ['start_pub', 'end_pub']



class Question(models.Model):
    KINDS = (
        ('a', 'ответ текстом'),
        ('b', 'ответ с выбором одного варианта'),
        ('c', 'ответ с выбором нескольких вариантов'),
    )
    poll = models.ForeignKey(Poll, verbose_name='опрос', blank=False, default=' ', null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000, blank=False, null=False, default=' ', verbose_name='текст вопроса')
    kind = models.CharField(max_length=1, choices=KINDS)

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'
