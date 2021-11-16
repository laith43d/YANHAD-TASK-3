import datetime

from ninja import Schema
from pydantic import UUID4



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

class ProductUpdate(Schema):
    id: UUID4
    is_featured: bool
    name: str
    description: str
    qty: int
    price: int
    discounted_price: int
    category_id: UUID4
    vendor_id: UUID4
    merchant_id: UUID4
    label_id: UUID4
    created: datetime.datetime
    updated: datetime.datetime

class AddToCartPayload(Schema):
    product_id: UUID4
    qty: int

class City(Schema):
    name: str

class AddressOut(Schema):
    id: UUID4
    work_address: bool
    address1: str
    address2: str
    city: City
    phone: str


class AddressIn(Schema):
    work_address: bool
    address1: str
    address2: str
    city_id: UUID4
    phone: str

class CheckOutIn(Schema):
    note: str=None
    address_id:UUID4
    status_id: UUID4