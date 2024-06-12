from rest_framework import serializers
from ..models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields = '__all__'
        

    # user=serializers.CharField(max_length = 150)
    # title=serializers.CharField(max_length = 150)
    # content=serializers.CharField(max_length=150)
    