from .views import UsersViewSet, CarfaxViewSet, UserEmailViewSet, RequestViewSet
from rest_framework import routers
from django.urls import path


router = routers.DefaultRouter()

router.register('users', UsersViewSet, basename='users')
# router.register('movie', MovieApiView, basename='movie')
router.register('email', UserEmailViewSet, basename="email")

router.register('car', CarfaxViewSet, basename='car')

router.register('request', RequestViewSet, basename='request')

urlpatterns = [
]

urlpatterns += router.urls