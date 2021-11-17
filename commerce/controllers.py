from typing import List

from django.shortcuts import get_object_or_404
from ninja import Router
from pydantic import UUID4
from django.contrib.auth import get_user_model

from account.authorization import GlobalAuth
from commerce.models import Product, Label, Merchant, Vendor, Category, Item
from commerce.schemas import ProductOut, ProductCreate, MessageOut, LabelOut, MerchantOut, CategoryOut, VendorOut, \
    AddToCartPayload

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


# create all crud operations for Label, Merchant, Vendor, Category

@commerce_controller.get('Merchants', response={
    200: List[MerchantOut],
})
def list_Merchants(request):
    merchants = Merchant.objects.all()
    return merchants


@commerce_controller.get('Merchants/{id}', response={
    200: MerchantOut
})
def retrieve_Merchant(request, id):
    return get_object_or_404(Merchant, id=id)


@commerce_controller.post('Merchants', auth=GlobalAuth(), response={
    201: MerchantOut,
    400: MessageOut
})
def create_Merchant(request, payload: MerchantOut):
    try:
        merchant = Merchant.objects.create(**payload.dict())
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, merchant


@commerce_controller.put('Merchant/{id}', auth=GlobalAuth(), )
def Merchant_employee(request, id, payload: MerchantOut):
    merchant = get_object_or_404(Merchant, id=id)
    for attr, value in payload.dict().items():
        setattr(merchant, attr, value)
    merchant.save()
    return {"success": True}


@commerce_controller.delete('merchant/{id}', auth=GlobalAuth(), )
def delete_merchant(request, id):
    merchant = get_object_or_404(Merchant, id=id)
    merchant.delete()

    return {"success": True}


# create all crud operations for Label, Merchant, Vendor, Category

@commerce_controller.get('Vendor', response={
    200: List[VendorOut],
})
def list_Vendors(request):
    vendors = Vendor.objects.all()
    return vendors


@commerce_controller.get('Vendors/{id}', response={
    200: VendorOut
})
def retrieve_Vendor(request, id):
    return get_object_or_404(Vendor, id=id)


@commerce_controller.post('Vendors', auth=GlobalAuth(), response={
    201: VendorOut,
    400: MessageOut
})
def create_Vendor(request, payload: VendorOut):
    try:
        vendor = Vendor.objects.create(**payload.dict())
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, vendor


@commerce_controller.put('Vendor/{id}', auth=GlobalAuth(), )
def Vendor_employee(request, id, payload: VendorOut):
    vendor = get_object_or_404(Vendor, id=id)
    for attr, value in payload.dict().items():
        setattr(vendor, attr, value)
    vendor.save()
    return {"success": True}


@commerce_controller.delete('Vendor/{id}', auth=GlobalAuth(), )
def delete_Vendor(request, id):
    vendor = get_object_or_404(Vendor, id=id)
    vendor.delete()

    return {"success": True}


# create all crud operations for Label, Merchant, Vendor, Category

@commerce_controller.get('Categorys', response={
    200: List[CategoryOut],
})
def list_Categorys(request):
    categorys = Category.objects.all()
    # Categorys = Categorys.filter(name='tshirt')
    return categorys


@commerce_controller.get('Categorys/{id}', response={
    200: CategoryOut
})
def retrieve_Category(request, id):
    return get_object_or_404(Category, id=id)


@commerce_controller.post('Categorys', auth=GlobalAuth(), response={
    201: CategoryOut,
    400: MessageOut
})
def create_Category(request, payload: CategoryOut):
    try:
        category = Category.objects.create(**payload.dict(), is_active=True)
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 201, category


@commerce_controller.put('Category/{id}', auth=GlobalAuth(), )
def Category_employee(request, id, payload: CategoryOut):
    category = get_object_or_404(Category, id=id)
    for attr, value in payload.dict().items():
        setattr(category, attr, value)
    category.save()
    return {"success": True}


@commerce_controller.delete('Category/{id}', auth=GlobalAuth())
def delete_Category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()

    return {"success": True}


@order_controller.post('add-to-cart', response=MessageOut, auth=GlobalAuth())
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


@order_controller.post('increase-item/{item_id}', auth=GlobalAuth(), response=MessageOut)
def increase_item_qty(request, item_id: UUID4):
    user = get_object_or_404(User, id=request.auth['pk'])
    item = get_object_or_404(Item, id=item_id, user=user)
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
