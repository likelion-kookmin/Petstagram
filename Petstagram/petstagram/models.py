from django.db import models

class Feed(models.Model):
    title = models.CharField(max_length=50)
    create_date = models.DateTimeField(null=True)
    writer = models.CharField(max_length=20, null=True)
    context = models.TextField()
    media = models.ImageField(upload_to="feed/", blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.text[:100]
