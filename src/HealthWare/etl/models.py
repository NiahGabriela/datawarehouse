from django.db import models

# universal select for different databases

class Query(models.Model):
    database = models.CharField(max_length=200)
    select = models.CharField(max_length=200)
    having = models.CharField(max_length=200)
    group = models.CharField(max_length=200)
    sort = models.CharField(max_length=200)
    where = models.CharField(max_length=200)
    nestedSelect = models.CharField(max_length=200)
