from django.urls import path, include
from ticadas import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'persons', views.TicadasViewSet)

urlpatterns= [
    path('',include(router.urls)),
]
