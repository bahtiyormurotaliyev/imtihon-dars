from django.db import models

class catalog(models.Model):
       title = models.CharField(max_length=100)
       description = models.TextField()
       body = models.TextField()

       def __str__(self):
           return self.title
   
