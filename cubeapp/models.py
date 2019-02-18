from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class RealObject(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    abbreviation = models.ForeignKey('Abbreviation', on_delete=models.CASCADE)
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name = "RealObject"
        verbose_name_plural = "RealObjects"

    def __str__(self):
        return self.name


class Abbreviation(models.Model):
    first = models.CharField(max_length=1)
    second = models.CharField(max_length=1)

    class Meta:
        verbose_name = "Abbreviation"
        verbose_name_plural = "Abbreviations"
        unique_together = (("first", "second"),)

    def __str__(self):
        return (self.first + self.second).upper()

    def get_absolute_url(self):
        return reverse('cubeapp:pair-detail', args=[self.pk])


class IllegalLetter(models.Model):
    letter = models.CharField(max_length=1)
    replace = models.CharField(max_length=1, blank=True)
    user = models.ForeignKey(User, on_delete='CASCADE')

    class Meta:
        verbose_name = 'IllegalLetter'
        verbose_name_plural = 'IllegalLetters'

    def __str__(self):
        return str(self.user) + ' ' + self.letter + '->' + self.replace
