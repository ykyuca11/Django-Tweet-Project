from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=200)
    like = models.IntegerField(default=0, editable=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    def __str__(self):
        return f"{self.username} : {self.message}"
    
class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'tweet')


