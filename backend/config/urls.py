from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from rest_framework_swagger.views import get_swagger_view

from api.views import  ProductView, CityView, FeedbackView


schema_view = get_swagger_view(title="API")
router = DefaultRouter()
router.register(r"products", ProductView, basename="products")
router.register(r"city", CityView, basename='city')
router.register(r"feedback", FeedbackView, basename='feedback')


urlpatterns = [
    path("admin/", admin.site.urls),
    path("swagger/", schema_view),
    path("landing/", include('front.urls'))
]

urlpatterns += router.urls


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
