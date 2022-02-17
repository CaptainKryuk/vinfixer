from .views import UsersViewSet, CarfaxViewSet
from rest_framework import routers
from django.urls import path


router = routers.DefaultRouter()

router.register('users', UsersViewSet, basename='users')
# router.register('movie', MovieApiView, basename='movie')

router.register('car', CarfaxViewSet, basename='car')

urlpatterns = [
]

urlpatterns += router.urls