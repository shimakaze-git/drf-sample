from django.urls import path, include
from rest_framework import routers
from .views import ArticleViewSet, MemberViewSet

router = routers.DefaultRouter()
router.register('members', MemberViewSet)
router.register('articles', ArticleViewSet)

urlpatterns = [
    path("", include(router.urls))
]
