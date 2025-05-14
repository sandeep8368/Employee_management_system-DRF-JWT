from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import studentViewSet

router = DefaultRouter()

router.register(r'student', studentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
