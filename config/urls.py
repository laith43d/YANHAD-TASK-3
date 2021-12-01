from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from account.controllers import account_controller
from commerce.controllers import commerce_controller, commerce_controller2, commerce_controller3, commerce_controller4, \
    commerce_controller5, order_controller,commerce_controller6

api = NinjaAPI()
api.add_router('auth', account_controller)
api.add_router('', commerce_controller2)
api.add_router('', commerce_controller3)
api.add_router('', commerce_controller4)
api.add_router('', commerce_controller5)
api.add_router('', commerce_controller6)
api.add_router('', commerce_controller)
api.add_router('order', order_controller)

urlpatterns = [
    path('api/', api.urls),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
