from rest_framework import serializers
from .models import User,Pet,Wallet

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id' ,'name')

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('id' ,'user', 'nickname')

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('id' ,'user', 'wallet_id')