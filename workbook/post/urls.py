from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name = 'post_list'),
	path('post/create', views.PostCreate.as_view(), name = 'post_create'),
	path('post/<int:pk>/detail', views.post_detail, name = 'post_detail'),
	path('post/<int:pk>/update', views.PostUpdate.as_view(), name = 'post_update'),
	path('post/<int:pk>/delete', views.PostDelete.as_view(), name = 'post_delete'),
]