from django.db import models

# Create your models here.
class wxInfo(models.Model):
    type=models.CharField(max_length=16)
    text=models.CharField(max_length=5120)
    frome=models.CharField(max_length=512)
    time=models.CharField(max_length=32)

    def __str__(self):
        return '(%s(%s))' % (self.frome,self.text)