from django.urls import path
from .views import PostList, PostDetail, CommentList

app_name = 'blog'

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('', PostList.as_view(), name='listcreate'),
    path('comment/', CommentList.as_view(), name='comment-create'),
]
