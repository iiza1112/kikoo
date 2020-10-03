from django.urls import path
from . import views

app_name ='tweet'

urlpatterns = [
    path('',views.PostListView.as_view(),name='index'),
    path('path/new',views.PostCreateView.as_view(),name='post-create')
]