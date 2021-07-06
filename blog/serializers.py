from blog.models import Blog
from rest_framework import serializers

class BlogSerialize(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"