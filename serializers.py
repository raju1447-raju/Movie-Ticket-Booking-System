from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie, Show, Booking
User=get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta: model=User; fields=('username','email','password')
    def create(self,vd): u=User(username=vd['username'],email=vd.get('email'));u.set_password(vd['password']);u.save();return u

class MovieSerializer(serializers.ModelSerializer):
    class Meta: model=Movie; fields='__all__'

class ShowSerializer(serializers.ModelSerializer):
    class Meta: model=Show; fields='__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta: model=Booking; fields='__all__'
