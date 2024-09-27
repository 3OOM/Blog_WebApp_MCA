from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tbl_blog'