from typing import List

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from ninja import Router
from pydantic import UUID4

from account.authorization import GlobalAuth
from commerce.models import Product, Item, Address, Order, OrderStatus
from commerce.schemas import ProductOut, ProductCreate, AddToCartPayload, ProductUpdate, AddressOut, AddressIn, \
    CheckOutIn
from config.utils.schemas import MessageOut
import random, string

User = get_user_model()

commerce_controller = Router(tags=['products'])
order_controller = Router(tags=['order'])
addresses_controller = Router(tags=['addresses'])

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
def list_products(request):
    products = Product.objects.all()
    # products = products.filter(name='tshirt')
    return products


@commerce_controller.get('products/{id}', response={
    200: ProductOut
})
def retrieve_product(request, id):
    return get_object_or_404(Product, id=id)


@commerce_controller.post('products', auth=GlobalAuth(), response={
    201: ProductOut,
    400: MessageOut
})
def create_product(request, payload: ProductCreate):
    try:
        user = get_object_or_404(User, id=request.auth['pk'])

        if not user.is_superuser:
            return 400, {'detail': 'you are not admin'}
        product = Product.objects.create(**payload.dict(), is_active=True)
    except :
        return 400, {'detail': 'something wrong happened!'}

    return 201, product


@commerce_controller.put('product/{id}', auth=GlobalAuth())
def update_product(request, id, payload: ProductUpdate):
    user = get_object_or_404(User, id=request.auth['pk'])

    if not user.is_superuser:
        return 400, {'detail': 'you are not admin'}
    product = get_object_or_404(Product, id=id, user=user)
    for attr, value in payload.dict().items():
        setattr(product, attr, value)
    product.save()
    return {"success": True}


@commerce_controller.delete('product/{id}', auth=GlobalAuth())
def delete_product(request, id):
    user = get_object_or_404(User, id=request.auth['pk'])

    if not user.is_superuser:
        return 400, {'detail': 'you are not admin'}
    product = get_object_or_404(Product, id=id, user=user)
    product.delete()
    return {"success": True}


# @commerce_controller.put('product/{id}')
# def update_product(request):
#     pass
#
#
# @commerce_controller.delete('product/{id}')
# def delete_product(request):
#     pass


# bonus task
# create all crud operations for Label, Merchant, Vendor, Category


@order_controller.post('add-to-cart', auth=GlobalAuth(), response=MessageOut)
def add_to_cart(request, payload: AddToCartPayload):
    payload_validated = payload.copy()
    if payload.qty < 1:
        payload_validated.qty = 1

    try:

        item = Item.objects.get(product_id=payload.product_id)
    except Item.DoesNotExist:
        user = get_object_or_404(User, id=request.auth['pk'])
        Item.objects.create(product_id=payload.product_id, user=user, item_qty=payload_validated.qty,
                            ordered=False)
        return 200, {'detail': 'item added to cart successfully!'}

    item.item_qty += payload_validated.qty
    item.save()
    return 200, {'detail': 'item qty updated successfully!'}


@order_controller.put('item/{id}/increase-quantity', auth=GlobalAuth(), response=MessageOut)
def increase_item_qty(request, item_id: UUID4):
    try:
        user = get_object_or_404(User, id=request.auth['pk'])
        item = get_object_or_404(Item, id=item_id, user=user)
        item.item_qty += 1
        item.save()
    except user.DoesNotExist:
        return 400, {'detail': 'error!'}

    return 200, {'detail': 'Item qty increased successfully!'}


@order_controller.put('item/{id}/decrease-quantity', auth=GlobalAuth(), response=MessageOut)
def decrease_item_qty(request, item_id: UUID4):
    try:
        user = get_object_or_404(User, id=request.auth['pk'])
        item = get_object_or_404(Item, id=item_id, user=user)
        if item.item_qty == 1:
            item.delete()
        else:
            item.item_qty -= 1
            item.save()
    except user.DoesNotExist:
        return 400, {'detail': 'error!'}

    return 200, {'detail': 'Item qty increased successfully!'}




@order_controller.post('create', auth=GlobalAuth(), response=MessageOut)
def create_order(request):
    user = get_object_or_404(User, id=request.auth['pk'])
    random_alpha = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    order = Order.objects.create(user=user, ref_code=random_alpha,ordered=True)
    order.total = order.order_total
    order.save()

    return 200, {'detail': 'orderd create successfully!'}




@order_controller.put('checkout/{order_id}', auth=GlobalAuth(), response=MessageOut)
def checkout_order(request,order_id,payload:CheckOutIn):
    try:
        user = get_object_or_404(User, id=request.auth['pk'])
        order = get_object_or_404(Order, id=order_id, user=user)

        for attr, value in payload.dict().items():
            setattr(order, attr, value)
        order.save()
    except user.DoesNotExist:
        return 400, {'detail': 'error!'}

    return 200, {'detail': 'orderd updated successfully!'}
'''
/api/addresses CRUDs
*create address
*retrieve address
*update address
*delete address
'''


@addresses_controller.get('addresses', response={
    200: List[AddressOut],
})
def list_address(request):
    addresses = Address.objects.all()
    return addresses


@addresses_controller.get('addresses/{id}', response={
    200: AddressOut
})
def retrieve_address(request, id):
    return get_object_or_404(Address, id=id)


@addresses_controller.post('addresses', auth=GlobalAuth(), response={
    201: AddressOut,
    400: MessageOut
})
def add_address(request, payload: AddressIn):
    try:
        user = get_object_or_404(User, id=request.auth['pk'])
        address = Address.objects.create(**payload.dict(),user=user)
    except Exception as inst:
        print(inst)
        return 400, {'detail': 'something wrong happened!'}

    return 201, address


@addresses_controller.put('addresses/{id}', auth=GlobalAuth())
def update_address(request, id, payload: AddressIn):
    user = get_object_or_404(User, id=request.auth['pk'])
    address = get_object_or_404(Address, id=id, user=user)
    for attr, value in payload.dict().items():
        setattr(address, attr, value)
    address.save()
    return {"success": True}


@addresses_controller.delete('addresses/{id}', auth=GlobalAuth())
def delete_address(request, id):
    user = get_object_or_404(User, id=request.auth['pk'])
    address = get_object_or_404(Address, id=id, user=user)
    address.delete()
    return {"success": True}


'''
* Decrease items qty
* Delete item from cart
* Create order
* Checkout

'''
