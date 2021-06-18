"""django_task1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task_app.views import FeedItemView, FeedItemUserView, RelatedItemUserView

urlpatterns = [
    path('', FeedItemView.as_view(), name='posts'),
    path('selfposts/', FeedItemUserView.as_view(), name='selfposts'),
    path('relatedposts/', RelatedItemUserView.as_view(), name='relatedposts'),
    path('admin/', admin.site.urls),

]
