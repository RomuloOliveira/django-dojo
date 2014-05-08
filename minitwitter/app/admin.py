from django.contrib import admin
from minitwitter.app.models import Tweet

class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Tweet info', {'fields': ['user', 'text']}),
        ('Date information', {'fields': ['timestamp']})
    ]

admin.site.register(Tweet, TweetAdmin)
