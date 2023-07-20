from django.db import models


class LegalForm(models.Model):
    name = models.CharField(max_length=64)
    short_name = models.CharField(max_length=16)

    def __str__(self):
        return str(self.name)


class Organization(models.Model):
    name = models.CharField(max_length=64)
    legal_form = models.ForeignKey(LegalForm, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)