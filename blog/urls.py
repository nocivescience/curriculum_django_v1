from django.urls import path
from . import views
app_name='blog'
urlpatterns=[
    path('',views.renderPosts,name='blog'),
    path('post_detail/', views.postDetail, name='posts'),
    # path('<int:post_id>',views.post_detail,name='post_detail'),
]