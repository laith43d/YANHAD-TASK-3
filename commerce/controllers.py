from typing import List

from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import get_object_or_404
from ninja import Router
from pydantic import UUID4

from account.authorization import GlobalAuth
from commerce.models import Product, Item
from commerce.schemas import ProductOut, ProductCreate, AddToCartPayload
from config.utils.schemas import MessageOut

User = get_user_model()

commerce_controller = Router(tags=['products'])
order_controller = Router(tags=['order'])

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


# @commerce_controller.put('product/{id}')
# def update_product(request):
#     pass
#
#
# @commerce_controller.delete('product/{id}')
# def delete_product(request):
#     pass


@order_controller.post('add-to-cart', response=MessageOut, auth=GlobalAuth())
def add_to_cart(request, payload: AddToCartPayload):
    user = get_object_or_404(User, user_id=request.auth['pk'])
    payload_validated = payload.copy()
    if payload.qty < 1:
        payload_validated.qty = 1

    try:
        item = Item.objects.get(product_id=payload.product_id)
    except Item.DoesNotExist:
        Item.objects.create(product_id=payload.product_id, user=user, item_qty=payload_validated.qty,
                            ordered=False)
        return 200, {'detail': 'item added to cart successfully!'}

    item.item_qty += payload_validated.qty
    item.save()
    return 200, {'detail': 'item qty updated successfully!'}


@order_controller.post('increase-item/{item_id}', response=MessageOut, auth=GlobalAuth())
def increase_item_qty(request, item_id: UUID4):
    user = get_object_or_404(User, user_id=request.auth['pk'])
    item = get_object_or_404(Item, id=item_id, user=user)
    item.item_qty += 1
    item.save()

    return 200, {'detail': 'Item qty increased successfully!'}


@order_controller.post('decrease-item/{item_id}', response=MessageOut, auth=GlobalAuth())
def decrease_item_qty(request, item_id: UUID4):
    user = get_object_or_404(User, user_id=request.auth['pk'])
    item = get_object_or_404(Item, id=item_id, user=user)
    if item.item_qty == 0:
        item.delete()
        return 200, {"derail": "Item deleted"}
    item.item_qty -= 1
    item.save()

    return 200, {'detail': 'Item qty decrease successfully!'}


'''
* Decrease items qty
* Delete item from cart
* Create order
* Checkout

'''
