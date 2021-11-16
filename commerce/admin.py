from django.contrib import admin

from commerce.models import (
    Product,
    Category,
    Label, Vendor, Merchant, Item, Address, City, Order, OrderStatus

)

admin.site.register(Product)
admin.site.register(Label)
admin.site.register(Category)
admin.site.register(Vendor)
admin.site.register(Merchant)
admin.site.register(Address)
admin.site.register(City)
admin.site.register(Order)
admin.site.register(OrderStatus)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'item_qty')


admin.site.register(Item, ItemAdmin)
