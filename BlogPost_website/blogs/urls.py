from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('create', views.create, name='create'),
    path("increaselikes/<int:id>",views.increaselikes, name='increaselikes'),
    path("post/edit/<int:post_id>", views.editpost, name = 'editpost'),
    path('delete/<int:post_id>/', views.delete_post, name='deletepost'),
]
