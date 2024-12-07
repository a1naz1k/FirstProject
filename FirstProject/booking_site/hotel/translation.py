from .models import Hotel, Room, Review, Booking
from modeltranslation.translator import TranslationOptions, register


@register(Hotel)
class MovieTranslationOptions(TranslationOptions):
    fields = ('hotel_name','hotel_address', 'description')


@register(Room)
class CountryTranslationOptions(TranslationOptions):
    fields = ('room_description',)


