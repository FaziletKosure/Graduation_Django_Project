from rest_framework import serializers
from .models import Post, Comment, Category, Like, PostView
from django.conf import settings


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'id')


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Comment
        fields = ('content', 'post_id',
                  'user',
                  'time_stamp')


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    author = serializers.CharField(source="author.username", read_only=True)
    category = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Post
        fields = (

            'id',
            'title',
            'author',
            'excerpt',
            'content',
            'image',
            'category',
            'status',
            'comment_count',
            'view_count',
            'like_count',
            'published',
            'comments',
        )


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Like
        fields = (
            "user",
            "post"
        )


class PostViewSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = PostView
        fields = (
            "user",
            "post",
            "time_stamp"
        )


class UserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('email', 'username', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}
