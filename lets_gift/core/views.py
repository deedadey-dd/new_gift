from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import User, Vendor, Item, ItemImage, Wishlist, WishlistItem, Contribution
from .serializers import UserSerializer, VendorSerializer, ItemSerializer, ItemImageSerializer, WishlistSerializer, WishlistItemSerializer, ContributionSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Wishlist, Vendor
from .forms import WishlistForm, EditProfileForm, UserRegisterForm, VendorRegisterForm
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [permissions.AllowAny]


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.AllowAny]


class ItemImageViewSet(viewsets.ModelViewSet):
    queryset = ItemImage.objects.all()
    serializer_class = ItemImageSerializer
    permission_classes = [permissions.AllowAny]


class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [permissions.AllowAny]


class WishlistItemViewSet(viewsets.ModelViewSet):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer
    permission_classes = [permissions.AllowAny]


class ContributionViewSet(viewsets.ModelViewSet):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer
    permission_classes = [permissions.AllowAny]


def index(request):
    return render(request, 'core/index.html')


def wishlist(request):
    return render(request, 'core/wishlist.html')


def all_wishlists(request):
    wishlists = Wishlist.objects.filter(expiry_date__gte=datetime.now())
    return render(request, 'core/all_wishlists.html', {'wishlists': wishlists})


@login_required
def create_wishlist(request):
    if request.method == 'POST':
        form = WishlistForm(request.POST)
        if form.is_valid():
            wishlist = form.save(commit=False)
            wishlist.user = request.user
            wishlist.save()
            return redirect('my_wishlists')
    else:
        form = WishlistForm()
    return render(request, 'core/create_wishlist.html', {'form': form})


@login_required
def my_wishlists(request):
    wishlists = Wishlist.objects.filter(user=request.user)
    return render(request, 'core/my_wishlists.html', {'wishlists': wishlists})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'core/edit_profile.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print("User is authenticated:", user.is_authenticated)
            return HttpResponseRedirect(request.GET.get('next', '/'))
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form': form})


def register_vendor(request):
    if request.method == 'POST':
        form = VendorRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = VendorRegisterForm()
    return render(request, 'core/register_vendor.html', {'form': form})


@login_required
def create_wishlist(request):
    if request.method == 'POST':
        form = WishlistForm(request.POST)
        if form.is_valid():
            wishlist = form.save(commit=False)
            wishlist.user = request.user
            wishlist.save()
            return redirect('my_wishlists')
    else:
        form = WishlistForm()
    return render(request, 'core/create_wishlist.html', {'form': form})
