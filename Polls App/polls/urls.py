from django.urls import path
from . import views
app_name='polls' 
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/',views.details,name='details'),
    path('add_question',views.add_question,name='add_question'),
    path('<int:question_id>/add_choice',views.add_choice,name='add_choice'),
]