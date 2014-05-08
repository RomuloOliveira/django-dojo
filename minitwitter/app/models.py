from django.db import models

# Create your models here.
class Tweet(models.Model):
    user = models.CharField(max_length=16)
    text = models.CharField(max_length=140)
    timestamp = models.DateTimeField()

    def __unicode__(self):
        return '@{}: \'{}\''.format(self.user, self.text)