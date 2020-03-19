from django.db import models


class TestModel(models.Model):
    test_text = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
