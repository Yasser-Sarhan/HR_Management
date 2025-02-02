from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
   path('', views.post_list, name='post_list'),
   path('<int:id>', views.post_details, name='post_details'),
   path('create', views.post_create, name='post_create'),
   path('<int:id>/edit', views.post_edit, name='post_edit'),
   path('cbv/', views.PostList.as_view(), name='post_list_cbv'),
   path('cbv/<int:pk>', views.PostDetail.as_view(), name='post_details_cbv'),
   path('new/', views.CreatePost.as_view(), name= 'create_post')
]