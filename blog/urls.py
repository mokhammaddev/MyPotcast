from django.urls import path
from .views import index, about, detail, episodes, views, like

app_name = 'blog'


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('views/<int:pk>/', views, name='views'),
    path('like/<int:pk>/', like, name='like'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('episodes/', episodes, name='episodes'),
]
