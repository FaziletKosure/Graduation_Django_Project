from rest_framework import serializers
from .models import Post, Comment, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'id')


class PostSerializer(serializers.ModelSerializer):

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
        )


# class CategorySerializer(serializers.ModelSerializer):
#     cats = PostSerializer(many=True, read_only=True)

#     class Meta:
#         model = Category
#         fields = ('name', 'id', 'cats')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content', 'post_id')


# class PostDetailSerializer(serializers.ModelSerializer):
#     content = CommentSerializer(many=True, read_only=True)

#     class Meta:
#         model = Post
#         fields = (
#             'id',
#             'title',
#             'author',
#             'excerpt',
#             'content',
#             'image',
#             'category',
#             'status',
#             'content',
#         )
