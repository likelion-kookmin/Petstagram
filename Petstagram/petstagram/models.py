from django.db import models

# Create your models here.
class Feed(models.Model):
    title = models.CharField(max_length=50)
    create_date = models.DateTimeField(null=True)
    author_name = models.CharField(default="", max_length=50)
    author_id = models.ForeignKey("account.CustomUser", on_delete=models.CASCADE)
    context = models.TextField()
    media = models.ImageField(upload_to="feed/", blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.text[:100]
