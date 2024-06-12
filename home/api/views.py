from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView
from .serializer import BlogSerializer
from ..models import Blog

class BlogListAPIView(ListAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer


class BlogDetailAPIView(RetrieveAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    lookup_field="pk"

class BlogDeleteAPIView(DestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    lookup_field="pk"

class BlogUpdateAPIView(UpdateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    lookup_field="pk"