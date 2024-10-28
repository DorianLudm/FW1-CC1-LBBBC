from django.db import models

class Collec(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    date = models.DateField(auto_now_add=True)

    def __str__ (self):
        return self.title