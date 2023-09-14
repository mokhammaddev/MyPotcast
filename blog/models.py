from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=222)
    images = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=222)

    def __str__(self):
        return self.title


class Season(models.Model):
    title = models.CharField(max_length=222)
    season_id = models.CharField(max_length=222)

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey("profile.Profile", on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=222)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    like = models.IntegerField()
    views = models.IntegerField()
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='article/')
    music = models.FileField(upload_to='music/')
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=222)
    author = models.ForeignKey('profile.Profile', on_delete=models.SET_NULL, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.author.user.get_full_name() == '':
            return f"{self.author.user.get_full_name()}'s comment"
        return f"{self.author.user.username}'s comment"


class Newsletter(models.Model):
    email = models.EmailField()

