from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    #name= models.CharField(max_length=100, default="")
    # slug = models.SlugField(max_length=200, unique=True) #This refers to the part of a URL which identifies a valid web address element with human-readable keywords. This is generally derived from the title of the page.
    author = models.ForeignKey(User, on_delete=models.CASCADE) #used to specify a one-to-many relationship to another database model (e.g. an article  has one author, but an author can make many articles). The "one" side of the relationship is the model that contains the "key" (models containing a "foreign key" referring to that "key", are on the "many" side of such a relationship).
    content = models.TextField() #This is the body of your article.
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_on']

        def __str__(self):
            return f"{self.title} {self.name} {self.created_on}"


class RelatedArticle(models.Model):
    article = models.ForeignKey('Article', related_name = 'related_articles', on_delete=models.CASCADE)
    author = models.CharField(max_length =200)
    title = models.CharField(max_length=100, default="")
    text = models. TextField()
    related_image = models.ImageField(upload_to='media/', null=True, blank=True)
    created_on = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.text}"

