from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'vendors', views.VendorViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'item-images', views.ItemImageViewSet)
router.register(r'wishlists', views.WishlistViewSet)
router.register(r'wishlist-items', views.WishlistItemViewSet)
router.register(r'contributions', views.ContributionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('all_wishlists/', views.all_wishlists, name='all_wishlists'),
    path('create_wishlist/', views.create_wishlist, name='create_wishlist'),
    path('my_wishlists/', views.my_wishlists, name='my_wishlists'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('register/vendor/', views.register_vendor, name='register_vendor'),
    path('create_wishlist/', views.create_wishlist, name='create_wishlist'),
]
