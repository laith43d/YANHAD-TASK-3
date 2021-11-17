
from django.contrib import admin

from commerce.models import (
    Product,
    Category,
    Label, Vendor, Merchant,

)

admin.site.register(Product)
admin.site.register(Label)
admin.site.register(Category)
admin.site.register(Vendor)
admin.site.register(Merchant)

