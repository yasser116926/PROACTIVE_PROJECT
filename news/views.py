from rest_framework import viewsets
from .models import News
from .serializers import NewsSerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsAdminOrReadOnly


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminOrReadOnly]
    # Only admins can create, update, delete; others can read only

from django.shortcuts import render, redirect
from .forms import NewsForm

def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news-list')  # we will define this next
    else:
        form = NewsForm()

    return render(request, 'news/create_news.html', {'form': form})

def news_list(request):
    news = News.objects.all().order_by('-created_at')
    return render(request, 'news/news_list.html', {'news': news})

