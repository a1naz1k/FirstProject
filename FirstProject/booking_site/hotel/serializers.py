from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel_video', 'hotel_image']


class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_number', 'rooms', 'room_price']


class HotelListSerializer(serializers.ModelSerializer):
    rooms = RoomListSerializer(read_only=True, many=True)
    class Meta:
        model = Hotel
        fields = ['hotel_name', 'country', 'stars', 'rooms']


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room_image', 'room']


class RoomDetailSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializer(read_only=True, many=True)

    class Meta:
        model = Room
        fields = ['room_number', 'rooms', 'room_images', 'room_price', 'room_types', 'reservation_status',
                  'room_description', 'all_inclusive']


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_images = HotelImageSerializer(read_only=True, many=True)
    rooms = RoomDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Hotel
        fields = ['owner', 'hotel_name', 'hotel_images', 'country', 'city', 'hotel_address', 'description', 'rooms', 'stars']