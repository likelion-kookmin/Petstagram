from django.db import models

class Feed(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.text[:100]
