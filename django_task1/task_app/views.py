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


class RelatedItemUserView(ListView):
    model = FeedItem
    template_name = 'task_app/posts.html'
    context_object_name = 'publisher'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = RegisteredUser.objects.filter(user_id=self.request.user.id).values("user_id")
            tracked_users = RegisteredUser.objects.filter(tracking__user_id__in=user).values("user_id")
            queryset = FeedItem.objects.filter(user_id__in=tracked_users)
            return queryset