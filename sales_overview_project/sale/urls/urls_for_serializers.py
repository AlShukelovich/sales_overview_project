from django.urls import path, include
from rest_framework import routers
from sale.views.views_for_serializers import SaleViewSet

router = routers.DefaultRouter()
router.register(r'sale', SaleViewSet)

urlpatterns = [
    path('', include(router.urls)),
   # path('todo_cache/', TodoListViewSet.as_view()),
]