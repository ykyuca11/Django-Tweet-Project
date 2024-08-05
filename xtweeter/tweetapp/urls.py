from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "tweetapp"

urlpatterns = [
    path("", views.listtweet, name="listtweet"),
    path("addtweet/", views.addTweet, name="addtweet"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("deletetweet/<int:id>", views.deletetweet, name="deletetweet"),
    path('addlike/<int:id>/', views.addlike, name='addlike'),
    path('removelike/<int:id>/', views.removelike, name='removelike'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
