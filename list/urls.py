from django.urls import path
from .views import blog

app_name = 'list'

urlpatterns = [
    path('', blog, name='blog')
]