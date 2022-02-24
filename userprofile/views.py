# views.py
from rest_framework import viewsets

from .serializers import UserSerializer, PetSerializer, WalletSerializer
from .models import User, Pet, Wallet


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all().order_by('nickname')
    serializer_class = PetSerializer

class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all().order_by('user')
    serializer_class = WalletSerializer