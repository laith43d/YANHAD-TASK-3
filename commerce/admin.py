from django.contrib import admin

from commerce.models import (
    Address,
    City,
    Order,
    OrderStatus,
    Product,
    Category,
    Label, Vendor, Merchant, Item,

)

admin.site.register(Product)
admin.site.register(Label)
admin.site.register(Category)
admin.site.register(Vendor)
admin.site.register(Merchant)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'item_qty')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'address1', 'address2','phone')

class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status','ordered','ref_code')

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(Item, ItemAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(City,CityAdmin)
admin.site.register(OrderStatus,StatusAdmin)
