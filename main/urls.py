from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'user_profile', views.UserProfileViewSet)
router.register(r'loan', views.LoanViewSet)
router.register(r'review', views.ReviewViewSet)
router.register(r'reservation', views.ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)), 
]