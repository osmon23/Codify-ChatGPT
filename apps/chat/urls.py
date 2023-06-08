from django.urls import path
from rest_framework import routers

from .views import MessageListView, MessageCreateView

router = routers.DefaultRouter()

router.register(r'list', MessageListView)
router.register(r'chat', MessageCreateView)

urlpatterns = router.urls
