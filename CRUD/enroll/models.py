from django.db import models

# Create your models here.

class Input(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    
    
    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email