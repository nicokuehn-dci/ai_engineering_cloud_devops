from django.contrib import admin
from django.urls import path
from blog.views import PostListView, lst_view, PostDetailView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('blog/', PostListView.as_view(), name='blog'), # take note of the name blog
    path('blog-func/', lst_view, name='blog-fbv'), # fbv => function based view
    path('blog/posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
