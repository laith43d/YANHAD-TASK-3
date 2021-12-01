import datetime

from ninja import Schema
from pydantic import UUID4


class CategoryOut(Schema):
    id: UUID4
    name: str
    description: str
    image: str


class LabelOut(Schema):
    id: UUID4
    name: str


class MerchantOut(Schema):
    id: UUID4
    name: str


class VendorOut(Schema):
    id: UUID4
    name: str
    image: str




class CategoryIn(Schema):
    name: str
    description: str
    image: str


class LabelIn(Schema):
    name: str


class MerchantIn(Schema):
    name: str


class VendorIn(Schema):
    name: str
    image: str

class AddressIn(Schema):
    user: UUID4
    work_address: bool
    address1: str
    address2: str
    city: str
    phone: str

class AddressOut(Schema):
    id: UUID4
    user: UUID4
    work_address: bool
    address1: str
    address2: str
    city: str
    phone: str





class HumanQualities(Schema):
    age: int
    height: int


class RuaaSchema(Schema):
    name: str
    specs: HumanQualities

class CategoryOut(Schema):
    id: UUID4
    name: str
    description: str
    image: str

class LabelOut(Schema):
    id: UUID4
    name: str

class MerchantOut(Schema):
    id: UUID4
    name: str
    created: datetime.datetime
    updated: datetime.datetime

class VendorOut(Schema):
    id: UUID4
    name: str
    image: str


class ProductOut(Schema):
    id: UUID4
    is_featured: bool
    name: str
    description: str
    qty: int
    price: int
    discounted_price: int
    category: CategoryOut
    vendor: VendorOut
    merchant: MerchantOut
    label: LabelOut
    created: datetime.datetime
    updated: datetime.datetime

class ProductCreate(Schema):
    is_featured: bool
    name: str
    description: str
    qty: int
    cost: int
    price: int
    discounted_price: int
    category_id: UUID4
    vendor_id: UUID4
    merchant_id: UUID4
    label_id: UUID4


class AddToCartPayload(Schema):
    product_id: UUID4
    qty: int

class CreateOrder(Schema):
    user_id: UUID4
    address_id: UUID4
    total: int
    status: UUID4
    note: str
    ref_code: str
    ordered: bool
    item_id: UUID4

class Checkout(Schema):
    ordered: bool


