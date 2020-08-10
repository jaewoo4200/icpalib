from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    regi_id = models.CharField(max_length=8, blank=True, null=True)
    status = models.CharField(max_length=5, blank=True, null=True)
    call_id = models.CharField(max_length=30, blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'book'