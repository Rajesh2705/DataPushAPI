from django.urls import path,include
from rest_framework.routers  import DefaultRouter
from .viewsets import UserViewSet, DestinationViewSet, HeaderViewSet
from .views import IncomingDataView

router = DefaultRouter()
router.register('accounts', UserViewSet, basename='account')
router.register('destinations', DestinationViewSet, basename='destination')
router.register('headers', HeaderViewSet, basename='header')

urlpatterns = [
    path('server/incoming_data/', IncomingDataView.as_view(), name='incoming_data'),
]

urlpatterns += router.urls