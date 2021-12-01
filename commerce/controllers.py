from typing import List

from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import get_object_or_404
from ninja import Router
from pydantic import UUID4

from account.authorization import GlobalAuth
from commerce.models import Product, Item, Category, Merchant, Vendor, Label, Address, Order
from commerce.schemas import ProductOut, ProductCreate, AddToCartPayload, CategoryOut, MerchantOut, LabelOut, \
    CategoryIn, VendorOut, VendorIn, MerchantIn, LabelIn, AddressIn, AddressOut, CreateOrder, Checkout
from config.utils.schemas import MessageOut

User = get_user_model()

commerce_controller = Router(tags=['products'])
order_controller = Router(tags=['order'])
commerce_controller2 = Router(tags=['category'])
commerce_controller3 = Router(tags=['Vendor'])
commerce_controller4 = Router(tags=['Merchant'])
commerce_controller5 = Router(tags=['Label'])
commerce_controller6 = Router(tags=['address'])

# @commerce_controller.get('products')
# def list_products(request, id: int = None):
#     return {'name': 'Ruaa  solved the task very late!!!!'}
#
#
# @commerce_controller.get('products/{id}')
# def retrieve_products(request, id: int):
#     return {'name': f'Ruaa  solved the task {id} days late '}
#
#
# @commerce_controller.post('products')
# def create_product(request, product_in: RuaaSchema):
#     return product_in.dict()


'''
/api/resource/{id}/

/api/resource?id=&name=&age=

{
    JSON
}
'''


@commerce_controller.get('products', response={
    200: List[ProductOut],
})
def list_products(request, q: str = None, price_lte: int = None, price_gte: int = None):
    products = Product.objects.all()

    if q:
        products = products.filter(
            Q(name__icontains=q) | Q(description__icontains=q)
        )

    if price_lte:
        products = products.filter(discounted_price__lte=price_lte)

    if price_gte:
        products = products.filter(discounted_price__gte=price_gte)

    return products


@commerce_controller.get('products/{id}', response={
    200: ProductOut
})
def retrieve_product(request, id):
    return get_object_or_404(Product, id=id)


@commerce_controller.post('products', response={
    201: ProductOut,
    400: MessageOut
})
def create_product(request, payload: ProductCreate):
    try:
        product = Product.objects.create(**payload.dict(), is_active=True)
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, product

@commerce_controller.put('product/{id}')
def update_product(request, id, payload: ProductCreate):
    productUpdate = get_object_or_404(Product, id=id)
    for attr, value in payload.dict().items():
        setattr(productUpdate, attr, value)
    productUpdate.save()
    return {"success": True}


@commerce_controller.delete('product/{id}')
def delete_product(request, id):
    productDelete = get_object_or_404(Product, id=id)
    productDelete.delete()
    return {"success": True}


# @commerce_controller.put('product/{id}')
# def update_product(request):
#     pass
#
#
# @commerce_controller.delete('product/{id}')
# def delete_product(request):
#     pass
@commerce_controller2.get('Category', response={
    200: List[CategoryOut],
})
def list_categories(request):
    categories = Category.objects.all()
    return categories


@commerce_controller2.get('categories/{id}', response={
    200: CategoryOut
})
def retrieve_category(request, id):
    return get_object_or_404(Category, id=id)


@commerce_controller2.post('category', response={
    201: CategoryOut,
    400: MessageOut
})
def create_category(request, payload: CategoryIn):
    try:
        category = Category.objects.create(**payload.dict(), is_active=True)
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, category


@commerce_controller2.put('category/{id}')
def update_category(request, id, payload: CategoryIn):
    categoryUpdate = get_object_or_404(Category, id=id)
    for attr, value in payload.dict().items():
        setattr(categoryUpdate, attr, value)
    categoryUpdate.save()
    return {"success": True}


@commerce_controller2.delete('category/{id}')
def delete_category(request, id):
    categoryDelete = get_object_or_404(Category, id=id)
    categoryDelete.delete()
    return {"success": True}


@commerce_controller3.get('Vendor', response={
    200: List[VendorOut],
})
def list_vendor(request):
    vendors = Vendor.objects.all()
    return vendors


@commerce_controller3.get('vendors/{id}', response={
    200: VendorOut
})
def retrieve_vendor(request, id):
    return get_object_or_404(Vendor, id=id)


@commerce_controller3.post('createVendor', response={
    201: VendorOut,
    400: MessageOut
})
def create_vendor(request, payload: VendorIn):
    try:
        vendorCreate = Vendor.objects.create(**payload.dict())
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, vendorCreate


@commerce_controller3.put('vendor/{id}')
def update_vendor(request, id, payload: VendorIn):
    vendorUpdate = get_object_or_404(Vendor, id=id)
    for attr, value in payload.dict().items():
        setattr(vendorUpdate, attr, value)
    vendorUpdate.save()
    return {"success": True}


@commerce_controller3.delete('vender/{id}')
def delete_vender(request, id):
    venderDelete = get_object_or_404(Vendor, id=id)
    venderDelete.delete()
    return {"success": True}


@commerce_controller4.get('Merchant', response={
    200: List[MerchantOut],
})
def list_merchant(request):
    merchants = Merchant.objects.all()
    return merchants


@commerce_controller4.get('Merchants/{id}', response={
    200: MerchantOut
})
def retrieve_merchant(request, id):
    return get_object_or_404(Merchant, id=id)


@commerce_controller4.post('createMerchant', response={
    201: MerchantOut,
    400: MessageOut
})
def create_merchant(request, payload: MerchantIn):
    try:
        merchantCreate = Merchant.objects.create(**payload.dict())
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, merchantCreate


@commerce_controller4.put('updateMerchant/{id}')
def update_merchant(request, id, payload: MerchantIn):
    merchantUpdate = get_object_or_404(Merchant, id=id)
    for attr, value in payload.dict().items():
        setattr(merchantUpdate, attr, value)
    merchantUpdate.save()
    return {"success": True}


@commerce_controller4.delete('DeleteMerchant/{id}')
def delete_merchant(request, id):
    merchantDelete = get_object_or_404(Merchant, id=id)
    merchantDelete.delete()
    return {"success": True}


@commerce_controller5.get('Label', response={
    200: List[LabelOut],
})
def list_label(request):
    labels = Label.objects.all()
    return labels


@commerce_controller5.get('Labels/{id}', response={
    200: LabelOut
})
def retrieve_label(request, id):
    return get_object_or_404(Label, id=id)


@commerce_controller5.post('label', response={
    201: LabelOut,
    400: MessageOut
})
def create_label(request, payload: LabelIn):
    try:
        labelCreat = Label.objects.create(**payload.dict())
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, labelCreat


@commerce_controller5.put('label/{id}')
def update_label(request, id, payload: LabelIn):
    labelUpdate = get_object_or_404(Label, id=id)
    for attr, value in payload.dict().items():
        setattr(labelUpdate, attr, value)
    labelUpdate.save()
    return {"success": True}


@commerce_controller5.delete('label/{id}')
def delete_label(request, id):
    labelDelete = get_object_or_404(Label, id=id)
    labelDelete.delete()
    return {"success": True}


@commerce_controller6.get('address', response={
    200: List[AddressOut],
})
def list_address(request):
    addresses = Address.objects.all()
    return addresses


@commerce_controller6.get('addresses/{id}', response={
    200: AddressOut
})
def retrieve_address(request, id):
    return get_object_or_404(Address, id=id)


@commerce_controller6.post('address', response={
    201: AddressOut,
    400: MessageOut
})
def create_address(request, payload: AddressIn):
    try:
        addressCreat = Label.objects.create(**payload.dict())
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, addressCreat


@commerce_controller6.put('address/{id}')
def update_address(request, id, payload: AddressIn):
    addressUpdate = get_object_or_404(Address, id=id)
    for attr, value in payload.dict().items():
        setattr(addressUpdate, attr, value)
    addressUpdate.save()
    return {"success": True}


@commerce_controller6.delete('address/{id}')
def delete_address(request, id):
    addressDelete = get_object_or_404(Address, id=id)
    addressDelete.delete()
    return {"success": True}




@order_controller.post('add-to-cart',auth=GlobalAuth(), response=MessageOut)
def add_to_cart(request, payload: AddToCartPayload):
    payload_validated = payload.copy()
    if payload.qty < 1:
        payload_validated.qty = 1

    try:
        item = Item.objects.get(product_id=payload.product_id)
    except Item.DoesNotExist:
        Item.objects.create(product_id=payload.product_id, user=User.objects.first(), item_qty=payload_validated.qty,
                            ordered=False)
        return 200, {'detail': 'item added to cart successfully!'}

    item.item_qty += payload_validated.qty
    item.save()
    return 200, {'detail': 'item qty updated successfully!'}


@order_controller.post('increase-item/{item_id}',auth=GlobalAuth(), response=MessageOut)
def increase_item_qty(request, item_id: UUID4):
    item = get_object_or_404(Item, id=item_id, user=User.objects.first())
    item.item_qty += 1
    item.save()

    return 200, {'detail': 'Item qty increased successfully!'}

@order_controller.post('decrease-item/{item_id}',auth=GlobalAuth(), response=MessageOut)
def decrease_item(request, item_id: UUID4):
    item = get_object_or_404(Item, id=item_id)
    if item.item_qty < 1:
        item.delete()
        return 200, {'detail': 'successfully'}
    item.item_qty -= 1
    item.save()
    return 200, {'detail': 'successfully'}


@order_controller.delete('item/{id}')
def delete_itemFromCart(request, id):
    itemFromCartDelete = get_object_or_404(Item, id=id)
    itemFromCartDelete.delete()
    return {"success": True}

@order_controller.post('create_order',auth=GlobalAuth() ,response=MessageOut)
def creat_Order(request, payload: CreateOrder):
    try:
        order = Order.objects.create(**payload.dict(), user_id=get_user_model)
    except:
        return 400, {'detail': 'something went wrong'}

    return 200, {'detail': 'Order is created '}

@order_controller.put('checkout/order_id',auth=GlobalAuth())
def checkout(request, order_id: UUID4):
    check = get_object_or_404(Order, id=order_id)
    check.ordered = True
    check.save()
    return 200, Checkout



'''
* Decrease items qty
* Delete item from cart
* Create order
* Checkout

'''