from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from account.controllers import account_controller
from commerce.controllers import commerce_controller, order_controller, addresses_controller

api = NinjaAPI()
api.add_router('auth', account_controller)
api.add_router('', commerce_controller)
api.add_router('order', order_controller)
api.add_router('address', addresses_controller)

urlpatterns = [
    path('api/', api.urls),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
