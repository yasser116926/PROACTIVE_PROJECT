from django.shortcuts import render, redirect
from .forms import PostForm
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from core.permissions import IsAdminOrReadOnly

# DRF ViewSet for API
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(is_active=True)  # Only active posts
    serializer_class = PostSerializer
    permission_classes = [IsAdminOrReadOnly]

# Admin form view
def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post-form')  # reload or redirect elsewhere
    else:
        form = PostForm()
    return render(request, 'admin/posts_form.html', {'form': form})


from rest_framework.decorators import action
from rest_framework.response import Response

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(is_active=True)
    serializer_class = PostSerializer
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=False, methods=['get'])
    def public(self, request):
        posts = Post.objects.filter(is_active=True).order_by('-published_date')
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)
