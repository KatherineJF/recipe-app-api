from django.urls import path, include
from rest_framework.routers import DefaultRouter

from botbegone import views

router = DefaultRouter()
router.register('tags', views.TagViewSet)

app_name = 'botbegone'

urlpatterns=[
path("",include(router.urls))
]
