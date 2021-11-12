# TASK 3

Task resolution process:

* Fork the repo
* Clone the forked repo to your local machine
* Resolve the task
* Commit your solution
* Push to GitHub
* create a pull request


# Task


This task in complimentary task for the ongoing project (COMMERCE).

Note: don't forget to 

`makemigrations` and `migrate`

`pip install -r requirements.txt`

## implement the following API endpoints

* receives the item id and increase the quantity accordingly
* this endpoint is extremely similar to the reduce-quantity endpoint

```http request
/api/orders/item/{id}/increase-quantity
```

* receives the item id and decrease the quantity accordingly
* you should delete the item when it's quantity reaches 0

```http request
/api/orders/item/{id}/decrease-quantity
```

## authenticate the required endpoints

* secure all API endpoints that requires authorization
* update the implementation accordingly, replace the hardcoded user with the respective implementation to retrieve the current user.

## Bonus Task

* create a create-order endpoint
* this endpoint should satisfy the following
  * create a new order
  * set ref_code to a randomly generated 6 alphanumeric value
  * take all current items (ordered=False) and add them to the recently created order
  * set added items (ordered field) to be True

```http request
/api/orders/create
```

* finish the addresses CRUD operations

```http request
/api/addresses
```

* create the checkout endpoint
  * you should be able to add an optional note
  * you should be able to add an address to the order
  * set (ordered field) to True, thus the order becomes sealed
  * change order status accordingly

```http request
/api/orders/checkout
```


# Workflow

* user lists the products
  * user can filter and search based on a specific criteria
* user clicks on (add to cart) and specify the qty
  * item is created (cart item)
  * user can increase the qty
  * user can decrease the qty
  * user can delete the item
* user can order (create-order)
* user can add his address (multip)
  * user can update address
  * user can delete address
* user can checkout (checkout)



## create order

* add items and mark (ordered) field as True
* add ref_number
* add NEW status
* calculate the total


## checkout 

* if this user has an active order
* add address
* accept note
* update the status
* mark order.ordered field as True

## addresses

* create addresses schema
* create crud operations