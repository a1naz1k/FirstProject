from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'


class HotelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotel_name', 'country', 'city', 'stars']


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel_image']


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_photos = HotelImageSerializer(read_only=True, many=True)
    class Meta:
        model = Hotel
        fields = ['hotel_name', 'country', 'city', 'stars', 'hotel_image', 'owner', 'description', 'address', 'hotel_video']


class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_number', 'room_price', 'type', 'hotel_room', 'all_inclusive']


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room_image']


class RoomDetailSerializer(serializers.ModelSerializer):
    room_photos = RoomImageSerializer(read_only=True, many=True)
    class Meta:
        model = Room
        fields = ['room_photos', 'room_number', 'hotel_room', 'room_price', 'type', 'all_inclusive', 'room_description']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
