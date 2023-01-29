from rest_framework import serializers

from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import  Product, City, Feedback, ProductImage, FeedbackImage




class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )


class ProductSerializer(serializers.ModelSerializer):

    images = ProductImageSerializer(source='productimage_set', many=True)
    class Meta:
        model = Product
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class FeedbackImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackImage
        fields = '__all__'

    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )

class FeedbackSerializer(serializers.ModelSerializer):

    images = FeedbackImageSerializer(source='feedbackimage_set', many=True)

    class Meta:
        model = Feedback
        fields = '__all__'