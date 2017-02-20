from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):   ## 'models.Model' means that it is a Django model and lets Django know that it should be saved in the database
    author = models.ForeignKey('auth.User') ## 'ForeignKey' link to another model
    title = models.CharField(max_length=200)## 'CharField' define text with limited number of char
    text = models.TextField()## 'TextField' for long text without a limit
    created_date = models.DateTimeField(default=timezone.now)    ## 'DateTimeField' this is a date and time
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):  ## 'def' a function or method
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
