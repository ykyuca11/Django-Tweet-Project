from django.shortcuts import render, redirect , get_object_or_404
from . import models 
from .models import Tweet, TweetLike #,Image
#from .forms import ImageForm
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# Create your views here.


def listtweet(request):
    all_tweets = Tweet.objects.all()
    tweets_with_likes = []

    for tweet in all_tweets:
        liked = False
        if request.user.is_authenticated:
            liked = TweetLike.objects.filter(user=request.user, tweet=tweet).exists()
        tweets_with_likes.append({"tweet": tweet, "liked": liked})

    context = {"tweets_with_likes": tweets_with_likes}
    return render(request, "tweetapp/listtweet.html", context)

@login_required(login_url="/login")
def addTweet(request):
    if request.method == 'POST':
        message = request.POST.get("message")
        image = request.FILES.get("image")  # Resim dosyasını al
        tweet = Tweet.objects.create(username=request.user, message=message, image=image)
        return redirect('tweetapp:listtweet')
    else:
        return render(request, 'tweetapp/addtweet.html')
    
  
@login_required
def deletetweet(request, id):
    tweet = models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:
        models.Tweet.objects.filter(id = id).delete()
        return redirect('tweetapp:listtweet')


@login_required(login_url="/login")
def addlike(request, id):
    tweet = get_object_or_404(Tweet, id=id)
    tweet_like, created = TweetLike.objects.get_or_create(user=request.user, tweet=tweet)
    if created:
        tweet.like += 1
        liked = True
        tweet.save()
    return redirect(reverse('tweetapp:listtweet'))

@login_required(login_url="/login")
def removelike(request, id):
    tweet = get_object_or_404(Tweet, id=id)
    tweet_like = TweetLike.objects.filter(user=request.user, tweet=tweet).first()
    if tweet_like:
        tweet_like.delete()
        tweet.like -= 1
        liked = False
        tweet.save()
    return redirect(reverse('tweetapp:listtweet'))








class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

