# listings/urls.py
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'listings', ListingViewSet, basename='listing')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = router.urls
