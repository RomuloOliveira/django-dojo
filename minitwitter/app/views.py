from django.shortcuts import render
from django.http import HttpResponse, Http404

from minitwitter.app.models import Tweet

def index(request):
    last_tweets = Tweet.objects.all()[:15]

    return render(request, 'tweets/index.html', {'last_tweets': last_tweets})

def show(request, user, tweet_id):
    try:
        tweet = Tweet.objects.get(id=tweet_id, user=user)
    except Tweet.DoesNotExist, e:
        raise Http404('Tweet not found')
    else:
        return HttpResponse('Here\'s your tweet: ' + str(tweet))

