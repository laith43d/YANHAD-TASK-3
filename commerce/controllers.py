from typing import List

from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import get_object_or_404
from ninja import Router
from pydantic import UUID4

from account.authorization import GlobalAuth
from commerce.models import Product, Label, Merchant, Vendor, Category, Item
from commerce.schemas import ProductOut, ProductCreate, MessageOut, LabelOut, MerchantOut, CategoryOut, VendorOut, \
    AddToCartPayload

User = get_user_model()

commerce_controller = Router(tags=['products'])
order_controller = Router(tags=['order'])
User = get_user_model()

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

@commerce_controller.post('products', auth=GlobalAuth(), response={
    201: ProductOut,
    400: MessageOut
})

def create_product(request, payload: ProductCreate):
    try:
        product = Product.objects.create(**payload.dict(), is_active=True)
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, product

@commerce_controller.put('product/{id}', auth=GlobalAuth(), )
def update_employee(request, id, payload: ProductCreate):
    product = get_object_or_404(Product, id=id)
    for attr, value in payload.dict().items():
        setattr(product, attr, value)
    product.save()
    return {"success": True}


@commerce_controller.delete('product/{id}', auth=GlobalAuth(), )
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()

    return {"success": True}


# create all crud operations for Label, Merchant, Vendor, Category

@commerce_controller.get('Label', response={
    200: List[LabelOut],
})
def list_label(request):
    label = Label.objects.all()
    # label = Label.filter(name='tshirt')
    return label


@commerce_controller.get('Label/{id}', response={
    200: LabelOut
})
def retrieve_Label(request, id):
    return get_object_or_404(Label, id=id)


@commerce_controller.post('Label', auth=GlobalAuth(), response={
    201: LabelOut,
    400: MessageOut
})
def create_Label(request, payload: LabelOut):
    try:
        label = Label.objects.create(**payload.dict())
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, label


@commerce_controller.put('Label/{id}', auth=GlobalAuth(), )
def Label_employee(request, id, payload: LabelOut):
    label = get_object_or_404(Label, id=id)
    for attr, value in payload.dict().items():
        setattr(label, attr, value)
    label.save()
    return {"success": True}


@commerce_controller.delete('Label/{id}', auth=GlobalAuth(), )
def delete_label(request, id):
    label = get_object_or_404(Label, id=id)
    label.delete()

    return {"success": True}


# bonus task
# create all crud operations for Label, Merchant, Vendor, Category

# @commerce_controller.put('product/{id}')
# def update_product(request):
#     pass
#
#
# @commerce_controller.delete('product/{id}')
# def delete_product(request):
#     pass



@order_controller.post('add-to-cart', response=MessageOut)
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


@order_controller.post('increase-item/{item_id}', response=MessageOut)
def increase_item_qty(request, item_id: UUID4):
    item = get_object_or_404(Item, id=item_id, user=User.objects.first())
    item.item_qty += 1
    item.save()

    return 200, {'detail': 'Item qty increased successfully!'}



@order_controller.post('decrease-item/{item_id}', auth=GlobalAuth(), response=MessageOut)
def decrease_item_qty(request, item_id: UUID4):
    user = get_object_or_404(User, id=request.auth['pk'])
    item = get_object_or_404(Item, id=item_id, user=user)
    item.item_qty -= 1
    if item.item_qty == 0:
        item.delete()
    else:
        item.save()
    return 200, {'detail': 'Item qty decreased successfully!'}
'''
* Decrease items qty
* Delete item from cart
* Create order
* Checkout

'''