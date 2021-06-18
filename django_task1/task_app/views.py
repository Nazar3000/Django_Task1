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

class RelatedItemUserView(ListView):
    model = FeedItem
    template_name = 'task_app/posts.html'
    context_object_name = 'publisher'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            # user= FeedItem.objects.filter(user=self.request.user)
            user = RegisteredUser.objects.filter(id=self.request.user.id).values("user_id")
            # RegisteredUser.
            # tracking = user.tracking.get().values("user_id")
            tracked_users = RegisteredUser.objects.filter(tracked_by__user=user).values("user_id")
            # tracking = user1.objects.all().values("user_id")
            # tracking = RegisteredUser.tracking.all().values("user_id")

            queryset = FeedItem.objects.filter(user_id__in=tracked_users)


            # queryset = FeedItem.objects.filter(user_id__in=tracked_users)
            # queryset1= queryset.all()
            # queryset=FeedItem.objects.filter(user_id__in=user.tracking.all().values("user_id"))
            return queryset