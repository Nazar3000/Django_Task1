from django.shortcuts import render
# from models import FeedItem
from .models import FeedItem, RegisteredUser
from django.contrib.auth.models import User
from django.views.generic import ListView






class FeedItemView(ListView):
    model = FeedItem
    template_name = 'task_app/posts.html'
    context_object_name = 'publisher'
    queryset = FeedItem.objects.all()

class FeedItemUserView(ListView):
    model = FeedItem
    template_name = 'task_app/posts.html'
    context_object_name = 'publisher'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset=FeedItem.objects.filter(user=self.request.user)
            return queryset
        # return FeedItem.objects.filter(user=self.request.user)
    # if request.user.is_authenticated:
    #     FeedItem.objects.filter(user=request.user)
    # queryset = FeedItem.objects.filter(user=request.user)

