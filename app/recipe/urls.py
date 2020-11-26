from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views

route = DefaultRouter()
route.register('tags', views.TagViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(route.urls))
]
