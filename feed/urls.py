from django.urls import path
from .views import HomePageView,PostDetailView,AddPostView,delete_view

app_name = 'feed'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('post/', AddPostView.as_view(), name='post'),
    path('<id>/delete/', delete_view, name="delete" ),
]