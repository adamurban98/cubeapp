from django.db import models
from django.urls import reverse


class RealObject(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    abbreviation = models.ForeignKey('Abbreviation', on_delete=models.CASCADE)

    
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

    def __str__(self):
        return (self.first + self.second).upper()

    def get_absolute_url(self):
        return reverse('cubeapp:pair-detail', args=[self.pk])
