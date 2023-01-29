from django.contrib import admin

from .models import  Product, ProductImage, Feedback, FeedbackImage, City


admin.site.register(City)
admin.site.register(Product)
admin.site.register(Feedback)
admin.site.register(ProductImage)
admin.site.register(FeedbackImage)
