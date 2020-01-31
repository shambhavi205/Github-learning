from django.db import models

# Create your models here.


class Univercity(models.Model):
    name = models.CharField(max_length=30)


class Employee(models.Model):
    TITLE_CHOICES = [
        ('MR', 'Mr.'),
        ('MRS', 'Mrs.'),
        ('MS', 'Ms.')]
    title = models.CharField(max_length=3, choices=TITLE_CHOICES, default=False)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    age = models.IntegerField()
    univercity = models.ForeignKey(Univercity, on_delete=models.CASCADE(), default=False)

    def __str__(self):
        return self.name


